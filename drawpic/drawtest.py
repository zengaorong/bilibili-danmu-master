# -*-coding:utf8-*-
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

import sys
reload(sys)
sys.setdefaultencoding('utf-8')




def test_ts(ts, w, title='test_ts'):

    roll_mean = ts.rolling(window = w).mean()
    roll_std = ts.rolling(window = w).std()
    #pd_ewma = pd.ewma(ts, span=w)
    plt.clf()
    plt.figure()
    plt.grid()
    plt.plot(ts, color='blue',label='Original')
    plt.plot(roll_mean, color='red', label='Rolling Mean')
    plt.plot(roll_std, color='black', label = 'Rolling Std')
    #plt.plot(pd_ewma, color='yellow', label = 'EWMA')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')

    plt.savefig(title+'.png', format='png')
    plt.show()


data = pd.read_csv('test.csv', index_col='time')
#data = pd.read_csv('test.csv', index_col='time')
data.index = data.index
ts = data['data']
ts = ts[::-1]
print ts

test_ts(ts[0:50], 20, title='test_org')
# x = np.arange(0, 10, 0.2)
# y = np.sin(x)
#
# plt.plot(x, y)
# plt.show()

# x1 = np.linspace(0.0, 5.0)
# x2 = np.linspace(0.0, 3.0)
# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
# y2 = np.cos(2 * np.pi * x2)
# figure, ax1 = plt.subplots(1,1)
# # plt.subplots_adjust(left=0.14, bottom=0.1)
# # ax1 = figure.add_axes([0.14, 0.35, 0.77, 0.6 ])
# ax1.grid(True)
# ax1.plot(x1, y1, 'yo-', label="Test1")
# ax1.plot(x2, y2, 'r.-', label='Test2')
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
# plt.show()