import numpy as np
import pandas as pd

df = pd.read_csv("input.csv")
df = df.transform(np.sort)

df["dist"] = abs(df["L1"] - df["L2"])

sum = df["dist"].sum()

print(f"distance: {sum}")

counts = df["L2"].value_counts()

df["similarity"] = df["L1"] * df["L1"].map(counts)

sum = int(df["similarity"].sum())

print(f"similarity: {sum}")


# similarity
