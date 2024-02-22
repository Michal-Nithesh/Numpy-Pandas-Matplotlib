import pandas as pd
data = {'col1': [1 ,2 ,3 ,4 ,7], 'col2': [4 ,5 ,6 ,9 ,5], 'col3': [7 ,8 ,12 ,1 ,11]}
df = pd.DataFrame(data = data)
print("Orginal DataFrame")
print(df)
print("\nNumber of Columns :",len(df.columns))