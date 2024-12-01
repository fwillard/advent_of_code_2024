import numpy as np
import pandas as pd

df = pd.read_csv("input.csv")
df = df.transform(np.sort)

df["dist"] = abs(df["L1"] - df["L2"])

sum = df["dist"].sum()

print(sum)
