import pandas as pd
import matplotlib.pyplot as plt
import os
def _r(ds):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../csv/') + ds
    df = pd.DataFrame(pd.read_csv(path, index_col = 0))
    return df

def draw(city, year, mode):
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
    df[mode].plot()
    plt.savefig("./{0}-{1}.png".format(city, str(year)))
    plt.show()
    df.to_csv("test.csv")


draw('广安', 2020, "tH")