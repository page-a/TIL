### 미해결 질문
>## 키워드 별로 어떻게 하면 해당 키워드가 포함된 리뷰를 잘 분류할 수 있을까?

## Table of Contents
- [어제꺼_답안](#어제꺼_답안)
- [내일_질문](#내일_질문)
- [책_따라하기](#책_따라하기)



### 어제꺼_답안

- Q. 형태소를 크게 두가지로 분류하면?
  A. 명사처럼 혼자서 쓰일 수 있는 자립 형태소와 조사같이 혼자서 쓰일 수 없는 의존 형태소
- Q. NLP에서 normalization은?
  A. 같은 의미인데 표현법이 다른 것들을 처리하는 방법 USA = US



### 내일_질문

- Q. stemming과 lemmatization의 차이는?



### 책_따라하기

2. Text Preprocessing

  - [x] 어간 추출 Stemming

    - 어간 stem, 용언(동사, 형용사)를 활용할 때, 어미에 선생하는 부분 `잡/어간`
    - 어미 ending, 용언의 어간 뒤에 붙어서 변하는 부분, 문법적 기능을 수행 `다/어미`
    
- [x] 표제어 추출 Lemmatization

  - 표제어 추출, 기본 사전형 단어 추출

  - 단어들이 다른 형태를 가지더라도, 뿌리 단어를 찾는 것 `am, are, is` => `be`
  - 형태학적 형태소: 
    - 어간 Stem, 단어의 의미를 담고 있는 단어의 핵심 부분 `cats -> cat`
    - 접사 affix, 단어의 추가적인 의미를 주는 부분 `cats -> -s`

- [x] stem vs. lemma

  - 표제어 추출은 어간 추출과는 달리 단어의 형태가 적절히 보존되는 양상을 보이는 특징

  - 표제어 추출은 문맥을 고려하며, 수행했을 때의 결과는 해당 단어의 품사 정보를 보존합니다. (POS 태그를 보존한다고도 말할 수 있습니다.)

    하지만, 어간 추출을 수행한 결과는 품사 정보가 보존되지 않습니다. (다시 말해 POS 태그를 고려하지 않습니다.) 더 정확히는, 어간 추출을 한 결과는 사전에 존재하지 않는 단어일 경우가 많습니다.


