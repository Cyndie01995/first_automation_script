import pandas as pd
data = {"name": ["alice", "bob", "charlie"],
        "age": [25, 30, 35],
        "city": ["new york", "san francisco", "los angeles"],
        "visitors": ["chinaza", "ada", "obi"]
        }
df = pd.DataFrame(data)
df.to_csv("data.csv",index=False)

print(df)
df.to_excel("data.xlsx",index=False)

# df = pd.read_clipboard()
print(df)
# copy before you run