import json
import os
from basic_csv.basic_csv import load_json

def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Data/index.json"), encoding = "utf-8") as f:
        t = json.load(f)
        for k1 in t.keys():
            for k2 in t[k1].keys():
                path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Data{}").format(t[k1][k2]["path1"])
                print(path)
                load_json(path)

if __name__ == "__main__":
    main()
