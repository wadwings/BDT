import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import sys

def _r(ds):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../csv/') + ds
    df = pd.DataFrame(pd.read_csv(path, index_col = 0))
    return df

def draw(city, year, mode):
    year = int(year)
    df = _r(city + '.csv')
    sT = str(year) + '.01.01'
    flg = False
    for i in df.columns:
        if i == str(year) + '.12.31':
            flg = True
            eT = i
    if flg:
        df = df.iloc[df.index.get_loc("tH"):df.index.get_loc("tL") + 1, df.columns.get_loc(sT):df.columns.get_loc(eT)].astype(int)
    else:
        df = df.iloc[df.index.get_loc("tH"):df.index.get_loc("tL") + 1, df.columns.get_loc(sT):].astype(int)
    df.loc['ave_tem'] = df.apply((lambda x: (x/2).sum()))
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    df[mode].plot(rot=50, grid=True, fontsize=7)
    plt.savefig("{3}{0}-{1}-{2}.png".format(city, str(year), mode, os.path.join(os.path.dirname(os.path.abspath(__file__)),'../pic/')), dpi=400)
    plt.savefig("{3}{0}-{1}-{2}.png".format(city, str(year), mode, os.path.join(os.path.dirname(os.path.abspath(__file__)),'../web/main/pic/')), dpi=400)
    df.to_csv("{0}{1}.csv".format(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../log/'), str(time.time())))

if len(sys.argv) == 4:
    draw(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("arguments don't match the function")
    exit(-1)