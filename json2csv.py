import pandas as pd
import json

jsonfile = input("json file")
with open(jsonfile, "r", encoding="UTF-8") as f:
    jf = json.load(f)
q = []
a = []

for j in jf:
    q.append(j["instruction"])
    a.append(j["output"])

df = pd.DataFrame({'question': q,
                   'answer': a})
df.to_csv("dataset.csv", columns=['question', 'answer'], encoding="UTF-8")