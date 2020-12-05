### 미해결 질문
>## 키워드 별로 어떻게 하면 해당 키워드가 포함된 리뷰를 잘 분류할 수 있을까?

## Table of Contents
- [어제꺼_답안](#어제꺼_답안)
- [내일_질문](#내일_질문)
- [책_따라하기](#책_따라하기)



### 어제꺼_답안

- Q. 속성1안에 속성2들이 있는데 속성1은 여러종류가 있음 그 안에 또 속성2 존재   
  조건을 못찾을 시에 제일 마지막 속성에 있는 리뷰만 저장하게 만들려면?
  - A. 속성1의 len이랑 속성2의 len의 제일 끝이 될 떄 저장하게 하면 됨
- Q. excel에 텍스트 데이터를 텍스트 그대로 읽는 방법은?
  - A. `ast.literal_eval`
- Q. tuple list를 포함한 dict을 dataframe으로 바꾸는 방법은?
  - A. `pd.concat({k:pd.Series(v) for k,v in dict.items()}).reset_index()`



### 내일_질문

- Q. 형태소를 크게 두가지로 분류하면?
- Q. NLP에서 normalization은?



### 책_따라하기

- 2. Text Preprocessing

  - [x] Tokenization

    - 한국어 `KSS`(Korean Sentence Splitter)

      > 이거 써서 리뷰들 잘라내면 되겠다!

    - 형태소: 가장 작은 말의 단위

      - 문장: `에디가 딥러닝책을 읽었다.`
      - 자립 형태소: 그 자체로 단어가 됨(명사, 대명사, 수사 등), `'에디', '딥러닝책'`
      - 의존 형태소: 다른 형태소와 결합하여 사용됨(접사, 조사, 어간), `'-가','-을','읽-','-었','-다'`

    - 형태소 분석기별로 성능이 다름

  - [x] Cleaning and Normalization

    - 정규화 Normalization: 표현 방법이 다른 단어들을 통합시켜 같은 단어로 만듦, `'USA','US'`

    

