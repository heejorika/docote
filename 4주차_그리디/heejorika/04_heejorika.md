## 🔆문제 요약

- input
    - N : 어떠한 수 (2≤ N ≤ 100000)
        - N은 항상 K보다 크거간 같음
    - K : N을 나누기할 수 (2 ≤ K ≤ 100000)
- 문제 풀이
    
    1) N에서 1을 뺀다
    
    2) N을 K로 나눈다
    
- output
    - N이 1이 될 때까지 1 or 2번을 시행하는 횟수

## 🔆문제 풀이

- input
    - 자연수만 입력 받아야 하니 int(input())
    - N과, K를 한줄에 입력받아야 하니 split
    - try~except로 int로 변환 안 되는 값은 거르기
    - N가 K의 min, max값 확인
- count 변수에 N을 처리하는 횟수 카운팅
- N//K는 나누어 떨어지는 경우에는 N//K, 아니면 N-1

## 🔆기능 사항

- **number class**
    - N
    - K
    - N_MIN, N_MAX, K_MIN, K_MAX
- `inputNK()` : N과 K를 입력받는 함수, N과 K를 return 함
    - map(int, input().split())
        - 리스트 길이가 2개 맞는지도 확인
        - 자연수가 맞는지도 확인→ 아스키 코드 48~57
    - `checkNumMinMax(value)` : value의 min, max가 올바르면 True return
    - N이 K보다 크거나 같은 지 확인
- `inputValue()` : 숫자를 입력받을 함수

- **calculate class**
    - count : 실행 횟수
    - num : N, K 클래스
- `minus1(value)` : value를 -1해서 return
- `divisionNK(N, K)` : N을 K로 나누어 return
- `startCalculate()` : 계산 시작
    - 현재 N을 K로 나눌 수 있는지 파악
    - 실행 횟수 +1
- `run()` : 메인함수
    - number 클래스를 통해 N, K를 입력받음