import pandas as pd
import matplotlib.pyplot as plt
import os
import time as tm
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

def draw(city, month, mode):
    month = int(month)
    df = _r(city + '.csv')
    dataset = [
        [],
        [],
        []
    ]
    time = []
    for i in range(int(df[df.columns[0]]['year']), 2021):
        _m = '0'+str(month) if month < 10 else str(month)
        sT = str(i) + '.' + _m + '.01'
        for y in df.columns:
            if y == sT:
                flg = False
                for x in df.columns:
                    if x == str(i) + '.' + _m + '.' + str(day(i, month)):
                        flg = True
                        eT = x
                if flg:
                    tmp_df = df.iloc[df.index.get_loc("tH"):df.index.get_loc("tL") + 1, df.columns.get_loc(sT):df.columns.get_loc(eT)].astype(int)
                else:
                    tmp_df = df.iloc[df.index.get_loc("tH"):df.index.get_loc("tL") + 1, df.columns.get_loc(sT):].astype(int)
                tmp_df['total'] = tmp_df.apply(lambda x: (x/day(i, month)).sum(), axis = 1)
                tmp_df.loc['ave_tem'] = tmp_df.apply(lambda x: (x/2).sum())
                dataset[0].append(str(tmp_df['total'].tH))
                dataset[1].append(str(tmp_df['total'].tL))
                dataset[2].append(str(tmp_df['total'].ave_tem))
                time.append(str(i)+'.'+str(month))
    df = pd.DataFrame(data = dataset, index=['tH','tL','aT'], columns=time).astype(float)
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    df[mode].plot()
    plt.savefig("{2}{0}-{1}.png".format(city, str(month), os.path.join(os.path.dirname(os.path.abspath(__file__)),'../pic/')), dpi=400)
    df.to_csv("{0}{1}.csv".format(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../log/'), str(tm.time())))


if len(sys.argv) == 4:
    draw(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("arguments don't match the function")
    exit(-1)