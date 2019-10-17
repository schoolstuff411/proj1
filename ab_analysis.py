import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature?" p-value: {more_users_p:.3g}\n'
    '"Did users search more/less?" p-value: {more_searches_p:.3g}\n'
    '"Did more/less instructors use the search feature?" p-value: {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" p-value: {more_instr_searches_p:.3g}'
)

def main():
    searchdata_file = pd.read_json(sys.argv[1], orient='records', lines=True)
    #print(searchdata_file)
    # Must seperate odd/even user ids 
    # Odd uid were shown a new-and-improved search box.
    # Even were shown the original design

    """
    Chi table is:
    
                      used search ,   did not use search
    control
    treatment
    
    """
    
    
    searchdata_oldDesign_users = searchdata_file[searchdata_file["uid"] % 2 == 0]
    searchdata_newDesign_users = searchdata_file[searchdata_file["uid"] % 2 != 0]
    
    searchdata_oldDesign_users_yesSearch = searchdata_oldDesign_users[searchdata_oldDesign_users["search_count"] > 0]
    searchdata_oldDesign_users_noSearch =  searchdata_oldDesign_users[searchdata_oldDesign_users["search_count"] == 0]
    
    searchdata_newDesign_users_yesSearch = searchdata_newDesign_users[searchdata_newDesign_users["search_count"] > 0]
    searchdata_newDesign_users_noSearch = searchdata_newDesign_users[searchdata_newDesign_users["search_count"] == 0]
    
    

   
    contingency_more_users = [ 
                                [searchdata_oldDesign_users_yesSearch.shape[0], searchdata_oldDesign_users_noSearch.shape[0]],
                                [searchdata_newDesign_users_yesSearch.shape[0], searchdata_newDesign_users_noSearch.shape[0]]
                             ]
    
    chi2, more_users_p, dof, expected = stats.chi2_contingency(contingency_more_users)
    ######################
    
    searchdata_oldDesign_instructors = searchdata_oldDesign_users[searchdata_oldDesign_users["is_instructor"] == True]
    searchdata_newDesign_instructors = searchdata_newDesign_users[searchdata_newDesign_users["is_instructor"] == True]
    
    searchdata_oldDesign_instructors_yesSearch = searchdata_oldDesign_instructors[searchdata_oldDesign_instructors["search_count"] > 0]
    searchdata_oldDesign_instructors_noSearch =  searchdata_oldDesign_instructors[searchdata_oldDesign_instructors["search_count"] == 0]
    
    searchdata_newDesign_instructors_yesSearch = searchdata_newDesign_instructors[searchdata_newDesign_instructors["search_count"] > 0]
    searchdata_newDesign_instructors_noSearch = searchdata_newDesign_instructors[searchdata_newDesign_instructors["search_count"] == 0]
    
   
    
    contingency_more_instr = [ 
                                [searchdata_oldDesign_instructors_yesSearch.shape[0], searchdata_oldDesign_instructors_noSearch.shape[0]],
                                [searchdata_newDesign_instructors_yesSearch.shape[0], searchdata_newDesign_instructors_noSearch.shape[0]]
                             ]

    chi2,  more_instr_p, dof, expected = stats.chi2_contingency(contingency_more_instr)
    ########################
  
    print(OUTPUT_TEMPLATE.format(
        more_users_p=more_users_p,
        more_searches_p=stats.mannwhitneyu(searchdata_oldDesign_users_yesSearch["search_count"], searchdata_newDesign_users_yesSearch["search_count"]).pvalue,
        more_instr_p= more_instr_p,
        more_instr_searches_p=stats.mannwhitneyu(searchdata_oldDesign_instructors_yesSearch["search_count"], searchdata_newDesign_instructors_yesSearch["search_count"]).pvalue,
    ))


if __name__ == '__main__':
    main()