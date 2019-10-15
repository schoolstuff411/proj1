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

    # Output
    searchdata_oldDesign_users = searchdata_file[searchdata_file["uid"] % 2 == 0]
    searchdata_newDesign_users = searchdata_file[searchdata_file["uid"] % 2 != 0]
    
    searchdata_oldDesign_instructors = searchdata_oldDesign_users[searchdata_oldDesign_users["is_instructor"] == True]
    searchdata_newDesign_instructors = searchdata_newDesign_users[searchdata_newDesign_users["is_instructor"] == True]
    
    print(searchdata_oldDesign_users)
    #Did more users use the search feature? 
    #(More precisely: did a different fraction of users have search count > 0?)
    #Did users search more often? 
    #(More precisely: is the number of searches per user different?)
    
    
    #chi-squared test works on categorical totals like
    #First one is chi as our categories are: Used search or didnt use search
    
    #mwu as it can be used to decide that samples from one group are larger/​smaller than another
    #
    print(OUTPUT_TEMPLATE.format(
        more_users_p=0,
        more_searches_p=0,
        more_instr_p=0,
        more_instr_searches_p=0,
    ))


if __name__ == '__main__':
    main()