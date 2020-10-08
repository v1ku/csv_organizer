import csv
import os
import pandas as pd


name_df = pd.read_csv('./csv/keys.csv')
directory = './csv/inputs'
df_list = []
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        to_check_df = pd.read_csv(directory+'/'+filename)
        result=name_df.merge(to_check_df,on = 'Name')
        result['source'] = filename
        df_list.append(result)

organized_df = pd.concat(df_list)
organized_df.reset_index(drop=True, inplace=True)
organized_df.to_csv("./csv/output.csv")

        


  