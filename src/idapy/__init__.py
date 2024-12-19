import pandas as pd
import cupy as cp
iscuda = cp.cuda.runtime.getDeviceCount() > 0
pd.options.display.float_format = '{:.3f}'.format