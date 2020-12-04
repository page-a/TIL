#%%
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
import argparse
from ckonlpy.tag import Twitter
from ckonlpy.tag import Postprocessor
twitter = Twitter()
import ast


# 각 attr keyword가 review에 포함되면 각 attr에 해당하는 review들을 분류
#%%
attr_df=pd.read_excel(Path("G:/공유 드라이브/속성사전/Data/Electronics/RiceCooker/2. Seed D_전기밥솥_copy_jk_20201130.xlsx")
                ,sheet_name='1B')
review_df=pd.read_csv(Path("G:/공유 드라이브/속성사전/Data/Electronics/RiceCooker/review_20201129.csv"))

review_list=[(body,rating)for body, rating in zip(review_df['body'],review_df['rating'])]

# %%
#attr별로 리뷰 모아주려고 만든 dict
cooker_review = {}
for attr in attr_df['attrs']:
    cooker_review[attr]=[]

#attr별로 filter 1차로 걸 키워드 모아놓은 dict


cooker_filter = {}
for _, _attr, _filter in attr_df[['attrs','filter_1']].itertuples():
    cooker_filter[_attr]=ast.literal_eval(_filter)

#review_list에서 분류되지 않은 남은 리뷰들 넣는 list
remain_review = []
# for body in review_list[6:9]:
n_review_list_end=len(review_list)
n_review_list_start=1

for body in review_list:
    n_review_list_start+=1
    print(n_review_list_start/n_review_list_end*100)
    # print('\n=====body 시작=====')
    # print('    문장: ', body[0])
    attrBreak = False
    filter_1Break = False
    
    n_attr_start = 1
    n_attr_end = len(cooker_filter)
    for attr in cooker_filter:
        # print('attr:', attr)

        n_attr_start+=1

        n_filter_1_start=1
        n_filter_1_end=len(cooker_filter[attr])
        for filter_1 in cooker_filter[attr]:
            # print('  1차필터: ',filter_1)
            if filter_1 in body[0]:
                # print(f'     1차필터는 "{body[0]}"에 포함된다')
                cooker_review[attr].append(body)
                attrBreak=True
                # 한 리뷰에 하나의 attr_2가 들어감
                break

            else:
                n_filter_1_start+=1
                #제일 마지막으로 남은 리뷰만 저장하기 위함
                if (n_filter_1_start == n_filter_1_end) and (n_attr_start == n_attr_end):
                    remain_review.append(body)
                # continue
        
        if attrBreak is True: #다음 리뷰로 이동
            break

print('\n*** 분류된 문서 ***\n', cooker_review)
print('\n*** 분류되지 않은 문서 ***\n', remain_review)

#%%
temp=pd.concat({k:pd.Series(v) for k,v in cooker_review.items()}).reset_index()
temp['body']=[_tuple[0] for _tuple in temp[0]]
temp['rating']=[_tuple[1] for _tuple in temp[0]]
temp.drop(columns=['level_1',0], inplace=True)
temp.columns = ['attr_2','name','rating']

#%%
########## 4,5점 긍정 - 1,2점 부정으로 옮기기 ########
attr_pos = {}
for attr in attr_df['attrs']:
    attr_pos[attr]=[]
attr_neg = {}
for attr in attr_df['attrs']:
    attr_neg[attr]=[]

for _,attr,body, rating in temp.itertuples():
    if rating in [4,5]:

        attr_pos[attr].append(body)
    elif rating in [1,2]:
        attr_neg[attr].append(body)
    else:
        pass
        

for attr in attr_pos:
    attr_pos[attr]='; '.join(attr_pos[attr])
for attr in attr_neg:
    attr_neg[attr]='; '.join(attr_neg[attr])


pos_neg = pd.concat([pd.DataFrame.from_dict(attr_pos,orient='index',columns=['pos'])
,pd.DataFrame.from_dict(attr_neg,orient='index',columns=['neg'])]
, axis = 1)


# %%
#### attr별 카운트 구하기#####
cooker_review_attr_count = {}
for key in cooker_review.keys():
    cooker_review_attr_count[key] = len(cooker_review[key])
attr2_count_df=pd.DataFrame.from_dict(cooker_review_attr_count,orient='index',columns=['count'])
pd.concat([pos_neg, attr2_count_df],axis=1).to_excel('./temp.xlsx')
# %%

#%%
# '알려진' in '안알려진'
# twitter.pos('안알려진', stem=True, norm=True)

#%%
# twitter.pos('가벼움', stem=True, norm=True)

# twitter.add_dictionary(['가볍다','가벼움','가벼워서'], 'keyword', force=True)
# twitter.pos('솥이 가벼워서 괜찮아요', stem=True, norm=True)
# twitter.pos('바람이 정말 세서', stem=True, norm=True)
# twitter.add_dictionary(['풀스텐','풀스텐 커버','가벼워서'], 'keyword', force=True)
# twitter.pos('솥이 가벼워서 괜찮아요', stem=True, norm=True)


#%%
# # ['가벼' in body for body in body_list]
# def f0002():
#     # passtags = {'Keyword'}
#     # postprocessor = Postprocessor(twitter, passtags = passtags)
#     # postprocessor.pos('풀스텐 내솥 내솥, 뚜껑 모두 스테인리스에 뚜껑 분리도 되는게 참 신기하네요. ')
#     # pass


 
# if __name__ == '__main__':
#     # f0001(args.FILE_PATH,args.EXPORT_PATH,args.FREQ_N)
#     f0002()


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