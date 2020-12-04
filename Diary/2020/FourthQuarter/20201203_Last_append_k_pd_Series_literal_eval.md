### 미해결 질문
>## 키워드 별로 어떻게 하면 해당 키워드가 포함된 리뷰를 잘 분류할 수 있을까?

## Table of Contents
- [어제꺼_답안](#어제꺼_답안)
- [내일_질문](#내일_질문)
- [사전추가#4](#사전추가#4)



### 어제꺼_답안

- Q. pop을 iterating하면서 생기는 문제점은?
  - iterating시작할 때 인덱스를 내부적으로 가지게 되는데 loop돌면서 지워버리면 그 인덱스가 invalidation해짐
- Q. nested for 에서 break을 하는 방법은?
  - break하면서 바깥 for loop에 걸리게 break variable하나 만들어줘야 함 안쪽 for에는 break쓰고 바깥 for는 break variable 만들어서 True로 assign해주면 됨



### 내일_질문

- Q. 속성1안에 속성2들이 있는데 속성1은 여러종류가 있음 그 안에 또 속성2 존재   
  	조건을 못찾을 시에 제일 마지막 속성에 있는 리뷰만 저장하게 만들려면?
  - 
- Q. excel에 텍스트 데이터를 텍스트 그대로 읽는 방법은?
  - 
- Q. tuple list를 포함한 dict을 dataframe으로 바꾸는 방법은?
  - 

### 사전추가#4

- 속성1안에 속성2들이 있는데 속성1은 여러종류가 있음 그 안에 또 속성2 존재   
  조건을 못찾을 시에 제일 마지막 속성에 있는 리뷰만 저장하게 만들어야 함

  - 속성1의 for에 순서와 속성2의 for의 순서가 제일 끝일 때, 그 리뷰를 append하는 방식으로 짜서 해결

    ```python
    n_attr1
    for 
    	n_attr2
    	for
    if (n_attr2_start == n_attr2_end) and (n_attr1_start == n_attr1_end):
    ```

    

- 테스트 샘플은 됐고 이제 데이터 가져와서 해보자read_excel

  - excel에 텍스트 데이터는 통으로 묶임 

    - 엑셀 상의 `가,나` 로 화면에 보이는 것을 파이썬으로 읽으면 `'가, 나'` 통으로 묶여서 처리 됨

      > eval로 키워드 가져가면서 검색하다 발견! 

      ```python 
      cooker_filter[_attr]=ast.literal_eval(_filter)
      ```

      

- tuple list를 포함한 dict을 dataframe으로 바꾸고 싶었음

  - `{'가':[('나',1),('다',1)], '나':[('나',1),]}` 이런 형식의 데이터였음

    > concat과 k: pd.Series를 저렇게 활용할 수도 있겠구나!! 

    ```python 
    temp=pd.concat({k:pd.Series(v) for k,v in cooker_review.items()}).reset_index()
    ```

    

