import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Column to check
column_to_check = 'B'

# Check if column is present
if column_to_check in df:
    print(f"{column_to_check} is present in the DataFrame.")
else:
    print(f"{column_to_check} is not present in the DataFrame.")