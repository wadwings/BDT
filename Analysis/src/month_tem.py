import pandas as pd
import matplotlib.pyplot as plt
import os

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
    df = _r(city + '.csv')
    if month < 10:
        sT = str(year) + '.0'  + str(month) + '.01'
        eT = str(year) + '.0'  + str(month) + '.' + str(day(year, month))
    else:
        sT = str(year) + '.'  + str(month) + '.01'
        eT = str(year) + '.'  + str(month) + '.' + str(day(year, month))
    df = df.iloc[df.index.get_loc("tH"):df.index.get_loc("tL") + 1, df.columns.get_loc(sT):df.columns.get_loc(eT)].astype(int)
    df.loc['ave_tem'] = df.apply((lambda x: (x/2).sum()))
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    df[mode].plot()
    plt.savefig("./{0}-{1}-{2}.png".format(city, str(year), str(month)))
    plt.show()
    df.to_csv("test.csv")
