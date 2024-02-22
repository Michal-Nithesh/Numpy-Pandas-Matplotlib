import pandas as pd
import numpy as np

exam_data = {'Name':['Roy','Dima','Shanks','james','Emily','Michal','Joel','Ben Beck','Marco','Zoro'], 
            'Score':[1, 3, 2, 3, 2, 3, 1, 1, 2,1], 
            'Quality':['Yes','No','Yes','Yes','No','Yes','Yes','No','No','Yes']}
lable = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data ,index = lable)
selected_data = df.loc[['b','d','g','f'],['Score','Quality']]
print("Selected Specific Columns and Rows :")
print(selected_data)
