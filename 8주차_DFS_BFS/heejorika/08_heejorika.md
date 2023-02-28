# 히정

## 🔆문제 요약

- input
    - N(얼음틀 세로길이=행), M(얼음틀 가로길이=열)
    - 0아니면 1로 이루어진 m길이의 숫자 n번 입력받음(공백x)
- output
    - 붙어있는 얼음틀 개수
    

---

## 🔆문제 풀이

- 참고할 그림
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8d5e30e9-5fdd-4997-be5e-2df7656b178d/Untitled.png)
    
- 값을 문자열로 입력 받아 리스트에 넣기
- 딕셔너리에 입력받은 값 중 0이 들어있는 인덱스를 아래와 같이 저장
    - key: 행
    - value: 열
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c03203d4-7a6d-4536-b1bb-96221204cab3/Untitled.png)
    
- key값 중 순차적이지 않은 부분 체크
    - ex) 4행인 얼음틀에서 key=0,1,3이면 3번 혼자 떨어져 있으므로 3행은 열만 검사하면 됨
        - 왜 열까지 검사해야되냐! 예시에서는 3행이 일자로 연결 되있지만 만약 [3][2]가 1일 경우 얼음틀이 2개가 될 수도 있으니까!
- 일단 행(key) 별로 순차적인 열(value)은 리스트로 묶어둠
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cf659c5-c266-408e-89ca-e52317fbe217/Untitled.png)
    
- key를 다 돌았다면 이젠 인접한 행 2개를 비교함
    - 이때 덩어리끼리 비교하면 됨
    - 물론 이딴 경우도 존재하므로, 리스트 내 저 인덱스 번호가 있는 지 확인해야 됨
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab9a3582-f0d7-474b-a2a9-8afed73adff9/Untitled.png)
        
    - 그리고 인접한 행 모두를 비교해야 하는데 2개씩 하는거임
        - 2개 비교해서 만약 열 단위로 덩어리가 됐는데 다음행에서 이어진게 없으면 COUNT+1
        - 다음행에 이어진 게 있으면 그 다음행에도 이어져있을 수 있으니까 일단 보류 리스트에 넣고 다시 검사

---

## 🔆기능 사항

- input은 검사하지 않겠어
    - 왜냐면 귀찮아!
- 전역 변수
    - `iceMoldCount` : output으로 내보낼 붙어있는 얼음틀 개수
    - `inputValueDict` : 입력 값을 행과 열 단위로 분리하여 저장한 딕셔너리
- `classify_inputValue(inputValue)` : 처음 입력값을 딕셔너리로 분리
    - 1차원 리스트 내 저장된 문자열을 돌면서
        - 이때 key값은 리스트 내 문자열 인덱스임
        - 0인 부분만 value 리스트에 저장하여 반환
- `classify_sequentialInpuList(inputValueDict)` : 행별로 순차적인 열을 리스트로 묶기
- `check_sequentialRow(inputValueDict)` : key값 중 순차적이지 않은 부분 체크
    - key값들만 따로 빼서 보기
    - 만약에 순차적이지 않은 부분이 존재한다면 그 행(key)의 value리스트(2차원)의 행이 몇개인지 보고 inputMoldCount에 넣기
- `compare_sequentialRow(inputValueDict)` : 인접한 행 2개를 비교
    - 2개 비교해서 만약 열 단위로 덩어리가 됐는데 다음행에서 이어진게 없으면 COUNT+1
    - 다음행에 이어진 게 있으면 그 다음행에도 이어져있을 수 있으니까 일단 보류 리스트에 넣고 다시 검사