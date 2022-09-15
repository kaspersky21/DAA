import pandas as pd

df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 32, False],
    ['3', 'Steven', 40, True]])

df.columns = ['id','name','age','decision']
print(df)