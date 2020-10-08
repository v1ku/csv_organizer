import csv
import os
import pandas as pd
import argparse
import datetime

parser = argparse.ArgumentParser(description='Join csv files based on keys present in another input file')
parser.add_argument('-c','--criteria', help='csv file containing rows to filter input files')
parser.add_argument('-i','--inputs', help='path to folder containing input files')
parser.add_argument('-o','--output', help='path to output folder or output csv file')
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
if args.output[-4:] == '.csv':
    organized_df.to_csv(args.output)
else:
    time_now = datetime.datetime.now()
    op_file_name = args.output + '/' + time_now.strftime("%d-%m-%Y-%H-%M-%S.csv")
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    organized_df.to_csv(op_file_name)


        


  