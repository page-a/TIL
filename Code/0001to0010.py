#%%
import numpy as np
import pandas as pd
# from konlpy.tag import Okt ; okt = Okt()
from collections import Counter
from pathlib import Path
import argparse
from ckonlpy.tag import Twitter
from ckonlpy.tag import Postprocessor
twitter = Twitter()


# 각 attr keyword가 review에 포함되면 각 attr에 해당하는 review들을 분류

#%%
############# sample data ################
#별점이 포함된 리뷰(tuples list)를 카테고리별 조건(lists dict)에 맞게 분류

review = [('용량이 좋아요',1),('용량이 커서',2),('이건 넘어갈 문장',3)]
cooker_review = {}
cooker_filter = {}

attrs=['용량','압력수준']
for attr in attrs:
    cooker_review[attr]=[]
cooker_filter['용량'] = ['용량','인용']
cooker_filter['압력수준'] = ['기압']

remain_review = []

for body in review:
    print('\n=====body 시작=====')
    print('    문장: ', body[0])
    attrBreak = False
    for attr in attrs:
        for filter_1 in cooker_filter[attr]:
            print('  1차필터: ',filter_1)
            if filter_1 in body[0]:
                print(f'     1차필터는 "{body[0]}"에 포함된다')
                cooker_review[attr].append(body)
                attrBreak=True
                break
            else:
                remain_review.append(body)
                attrBreak=True
                break
        if attrBreak is True:
            break

print('\n*** 분류된 문서 ***\n', cooker_review)
print('\n*** 분류되지 않은 문서 ***\n', remain_review)


#%%
pd.read_excel("C:\Users\beluga\Desktop\TIL\Data\2. Seed D_전기밥솥_copy_jk_20201130.xlsx"
            ,sheet_name='1P')
    


# %%

#%%
# '알려진' in '안알려진'
twitter.pos('안알려진', stem=True, norm=True)
#%%
cooker = dict()
cooker['df']=['sd']

#%%
# twitter.pos('가벼움', stem=True, norm=True)

# twitter.add_dictionary(['가볍다','가벼움','가벼워서'], 'keyword', force=True)
# twitter.pos('솥이 가벼워서 괜찮아요', stem=True, norm=True)
# twitter.pos('바람이 정말 세서', stem=True, norm=True)
twitter.add_dictionary(['풀스텐','풀스텐 커버','가벼워서'], 'keyword', force=True)
twitter.pos('솥이 가벼워서 괜찮아요', stem=True, norm=True)


#%%
['가벼' in body for body in body_list]
def f0002():
    passtags = {'Keyword'}
    postprocessor = Postprocessor(twitter, passtags = passtags)
    postprocessor.pos('풀스텐 내솥 내솥, 뚜껑 모두 스테인리스에 뚜껑 분리도 되는게 참 신기하네요. ')
    pass


 
if __name__ == '__main__':
    # f0001(args.FILE_PATH,args.EXPORT_PATH,args.FREQ_N)
    f0002()


"""
# parser = argparse.ArgumentParser()
# parser.add_argument('--FILE_PATH','-in')
# parser.add_argument('--EXPORT_PATH','-out')
# parser.add_argument('--FREQ_N','-n', type=int)
# args = parser.parse_args()
# args.FILE_PATH = '../Data/eye_df.csv'
# args.EXPORT_PATH = '../Data/eye_df_count.xlsx'
# args.FREQ_N = 200

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
    # save excel
    temp_dict = dict(count)
    temp_df=pd.DataFrame({'keyword':temp_dict.keys(), 'count':temp_dict.values()})
    temp_df.sort_values(by='count',ascending=False,inplace=True)
    temp_df.to_excel(Path(EXPORT_PATH),index=False)
    return 

# count_200=f0001('../Data/BabyProducts/MilkPowder/분유.csv'
#                 ,'../Data/BabyProducts/MilkPowder/_분유_count.xlsx'
#                 ,200)
"""