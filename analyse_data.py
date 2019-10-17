import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

pd.set_option('display.float_format', lambda x: '%.7f' % x)
data_df = pd.read_csv("data.csv");
#print(data_df.to_string())

anova = stats.f_oneway(data_df.iloc[0:,0].tolist(), 
                       data_df.iloc[0:,1].tolist(),
                       data_df.iloc[0:,2].tolist(),
                       data_df.iloc[0:,3].tolist(),
                       data_df.iloc[0:,4].tolist(),
                       data_df.iloc[0:,5].tolist(),
                       data_df.iloc[0:,6].tolist()
                      )
print(anova)
print(anova.pvalue)

x_melt = pd.melt(data_df)
posthoc = pairwise_tukeyhsd(
    x_melt['value'], x_melt['variable'],
    alpha=0.05)

print(posthoc)
fig = posthoc.plot_simultaneous()

