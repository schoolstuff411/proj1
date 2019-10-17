import time
from implementations import all_implementations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.DataFrame(columns=['qs1','qs2','qs3','qs4','qs5','merge1','partition_sort'])
 
time_results = [] 

print("This should take less than a minute")
for x in range(45):
    random_array = np.random.randint(9999, size=15000)
    for sort in all_implementations:
        st = time.time()
        res = sort(random_array)
        #print(res)
        en = time.time()
        time_results.append(en - st)
        
    s = pd.Series(time_results, index=df.columns)
    df = df.append(s, ignore_index=True)
    time_results = []
 
print("\n")
print("Finished")
pd.set_option('display.float_format', lambda x: '%.7f' % x)
print(df.to_string())
df.to_csv('data.csv', index=False)


