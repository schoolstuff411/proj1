import time
from implementations import all_implementations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


random_array = np.random.randint(99, size=9999)



# we need at least 40 data points. Does this mean i need to run each sorting
#function at least 40 times?
for sort in all_implementations:
    st = time.time()
    res = sort(random_array)
    #print(res)
    en = time.time()
    print(en)


