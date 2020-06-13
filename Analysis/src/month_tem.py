
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import sys

def day(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        days[1] = 29
    return days[month - 1]

def _r(ds):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../csv/') + ds
    df = pd.DataFrame(pd.read_csv(path, index_col = 0))
    return df

def draw(city, year, month, mode):
    year = int(year)
    month = int(month)
    df = _r(city + '.csv')
    if month < 10:
        sT = '{0}.0{1}.01'.format(str(year), str(month))
        eT = '{0}.0{1}.{2}'.format(str(year), str(month), str(day(year, month)))
    else:
        sT = str(year) + '.'  + str(month) + '.01'
        eT = str(year) + '.'  + str(month) + '.' + str(day(year, month))
    df = df.iloc[df.index.get_loc("tH"):df.index.get_loc("tL") + 1, df.columns.get_loc(sT):df.columns.get_loc(eT)].astype(int)
    df.loc['ave_tem'] = df.apply((lambda x: (x/2).sum()))
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    df[mode].plot(rot=50, grid=True, fontsize=7)
    plt.savefig("{4}{0}-{1}-{2}-{3}.png".format(city, str(year), str(month), mode, os.path.join(os.path.dirname(os.path.abspath(__file__)),'../pic/')), dpi=400)
    plt.savefig("{4}{0}-{1}-{2}-{3}.png".format(city, str(year), str(month), mode, os.path.join(os.path.dirname(os.path.abspath(__file__)),'../web/main/pic/')), dpi=400)
    df.to_csv("{0}{1}.csv".format(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../log/'), str(time.time())))

if len(sys.argv) == 5:
    draw(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
    print("arguments don't match the function")
    exit(-1)