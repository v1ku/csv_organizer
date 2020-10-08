import csv
import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Join csv files based on keys present in another input file')
parser.add_argument('--criteria', help='input file location')
parser.add_argument('--inputs', help='sum the integers (default: find the max)')
parser.add_argument('--output', help='sum the integers (default: find the max)')
args = parser.parse_args()

keys_df = pd.read_csv(args.criteria)
directory = args.inputs
df_list = []
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        to_check_df = pd.read_csv(directory+'/'+filename)
        result=pd.merge(to_check_df,keys_df,how='inner',on=keys_df.columns.values.tolist())
        result['source'] = filename
        df_list.append(result)

organized_df = pd.concat(df_list)
organized_df.reset_index(drop=True, inplace=True)
organized_df.to_csv(args.output)

        


  