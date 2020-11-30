#%%
import numpy as np
import pandas as pd
from konlpy.tag import Okt ; okt = Okt()
from collections import Counter
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--FILE_PATH','-in')
parser.add_argument('--EXPORT_PATH','-out')
parser.add_argument('--FREQ_N','-n', type=int)
args = parser.parse_args()
args.FILE_PATH = '../Data/eye_df.csv'
args.EXPORT_PATH = '../Data/eye_df_count.xlsx'
args.FREQ_N = 200

def f0001(FILE_PATH, EXPORT_PATH, FREQ_N=200):
    # Read Review File
    #  FILE_PATH = '../Data/BabyProducts/MilkPowder/분유.csv'
    review=pd.read_csv(Path(FILE_PATH))
    N_review = len(review)
    token_ls = []
    
    for i in range(2080,2083):
    # for i in range(N_review):
        # print(i)
        body = review['body'][i]
        if pd.isna(body):
            continue
        word_pos=okt.pos(body, stem=True, norm=True)
        [token_ls.append(token) for token, pos in word_pos if pos=='Noun']
    count_obj = Counter(token_ls)
    count = count_obj.most_common(FREQ_N)
#%%
    # save excel
    temp_dict = dict(count)
    temp_df=pd.DataFrame({'keyword':temp_dict.keys(), 'count':temp_dict.values()})
    temp_df.sort_values(by='count',ascending=False,inplace=True)
#%%
    temp_df.to_excel(Path(EXPORT_PATH),index=False)
    return 

# count_200=f0001('../Data/BabyProducts/MilkPowder/분유.csv'
#                 ,'../Data/BabyProducts/MilkPowder/_분유_count.xlsx'
#                 ,200)


 
if __name__ == '__main__':
    f0001(args.FILE_PATH,args.EXPORT_PATH,args.FREQ_N)