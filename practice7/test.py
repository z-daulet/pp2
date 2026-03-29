import pandas as pd
df =pd.read_csv("./phonebook.csv")
df2 = list(df[["username","first_name", "phone_number"]].itertuples(index=False,name=None))
for r in df2:
    print(r)