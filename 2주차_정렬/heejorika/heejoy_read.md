# 문제 풀이

## 🔆 문제 요약

- **입력 값**
    - 두 배열의 원소 N개
    - 배열 A, B
        - 원소는 모두 자연수
    - 바꿔칠 수 있는 횟수 K번
- **출력 값**
    - 배열 A의 모든 원소의 합이 최대가 될 수 있는 합

![image](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd1bf17a-7379-4841-bead-dc8be888737a/Untitled.png)

## 🔆예외 사항

- N과 K를 입력받을 때
    - N이 1이상 100,000이하 자연수인가
    - K가 0이상 N이하의 자연수인가(횟수니까)
    - 입력받을 때 길이가 2가 맞는가→ 아닐 경우 종료
    - 문자열이 들어갓을 경우
- 두 배열의 길이가 같은가
    - 배열의 모든 원소는 1이상 10,000,000보다 작은 자연수인가
    - 문자열이 들어갔을 경우

![image](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/20be3922-2f2f-4f44-a180-c18f729ab0b7/Untitled.png)

## 🔆기능 사항

- `inputAllValue()` : 필요한 입력값들을 입력받는 함수를 호출함
    - `inputNK()`
        - N : 1이상 100,000이하 자연수
        - K : 0이상 N이하의 자연수
    - `inputList()` : 배열의 모든 원소는 1이상 10,000,000보다 작은 자연수
- `changeValue()` : 바꿔치기하는 함수
    - a의 최솟값과 b의 최댓값을 바꿈
- `run()` : 해당 클래스를 돌리기 위한 함수

