import pandas as pd

df = pd.read_excel('Report2.xlsx' )
df_map = pd.read_excel("mapping file.xlsx")

df_join = pd.merge(df, df_map, left_on = "Country", right_on = "Country", how = "left")
df_join.to_excel("sample3.xlsx")

data = pd.DataFrame(df_join)

def changeValue(a, b):
    if a != b:
        return "Illegal Access"
    else:
        return a

data['Desc'] = data.apply(lambda row: changeValue(row['Access Type'], row['Print']), axis=1)

data.to_excel("Tugas_illegalaccess.xlsx")
print(data)