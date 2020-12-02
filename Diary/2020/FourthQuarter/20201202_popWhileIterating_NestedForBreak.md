### 미해결 질문
>## 키워드 별로 어떻게 하면 해당 키워드가 포함된 리뷰를 잘 분류할 수 있을까?

## Table of Contents
- [어제꺼_답안](#어제꺼_답안)
- [내일_질문](#내일_질문)
- [사전추가#3](#사전추가#3)

### 내일_질문
- Q. pop을 iterating하면서 생기는 문제점은?
- Q. nested for 에서 break을 하는 방법은?

### 사전추가#3

- 키워드를 찾은 리뷰는 삭제시키고 남은 리뷰들로 pos tagging하자

  - [ ] pop 써서 for문 돌리면서 처리

    > 3시간 넘게 짰는데 분명히 코드는 잘 짰는데... 의미도 맞는데 제대로 돌아가지 않음

    - [Remove elements from a list while iterating](https://thispointer.com/python-remove-elements-from-a-list-while-iterating/)

    - "we deleted an element from it while iterating over it, it will cause iterator invalidation and give unexpected results."

      

  - [ ] 분류할 리뷰, 남은 리뷰 따로 처리

    > for문을 3중으로 썼는데 다음 키워드로 넘어가야 하는데 넘어가지 않음
    - Break를 두 곳에다 줘야됨
      - 기존 if의 break + 바깥 for문에 attrBreak = False assign하고 안쪽 for문에 조건에 맞을 때 attrBreak를 True로 assign해야 함

