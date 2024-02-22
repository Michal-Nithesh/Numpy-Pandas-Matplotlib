import pandas as pd
Data = {'X':[78 ,85 ,96 ,90 ,86], 'Y':[84 ,94 ,89 ,83 ,86], 'Z':[86 ,97 ,96 ,72 ,83]}
df = pd.DataFrame(Data)

powers = [2, 3, 4]

result = [df.apply(lambda x: x ** powers)]

print(result)