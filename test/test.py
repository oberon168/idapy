import time
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
import idapy as da

pd.options.display.float_format = '{:.3f}'.format
test_data = pd.DataFrame(datasets.load_diabetes().data, columns=datasets.load_diabetes().feature_names)
test_target = pd.DataFrame(datasets.load_diabetes().target,columns=['prog'])
print(test_data.shape)
print(da.describe(test_data))
