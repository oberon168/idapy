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
    output = pd.dataFrame(columns=['Name','Size','Mean','StDev','Min','Max'])
    output.loc['Name'] = xdata.columns
    output.loc['Mean'] = xdata.mean()
    output.loc['StDev'] = xdata.std()
    output.loc['Min'] = xdata.min()
    output.loc['Max'] = xdata.max()
    print('sec:'end-start)
    return output


