# describe.py
import time
import pandas as pd

def describe(xdata, moments=False, quartiles=False, test=0):
    # quartiles add median and quartiles
    # moments add skewness and kurtosis
    # test  1 = t-test on each column with zero mean
    #       2 = Mann-Whitney-Wilcoxon test on each column with zero mean
    #       3 = Shapiro-Wilk(<2k)/Lilliefors(>2k) test for normality 
    #       4 = Lilliefors test for normality
    #       5 = Omnibus test for normality based on skewness and kutrosis
    start = time.time()
    output = pd.DataFrame(columns=['Name','Size','Mean','StDev','Min','Max'])
    output['Mean'] = xdata.mean()
    output['StDev'] = xdata.std()
    output['Min'] = xdata.min()
    output['Max'] = xdata.max()
    output['Size'] = xdata.count()
    output['Name'] = xdata.columns
    end = time.time()
    print('sec:',end-start)
    return output

