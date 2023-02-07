
import os   # os 모듈


# 상수 정의
N_MIN = 1; N_MAX = 1000000   # N 최소, 최대 정의
M_MIN = 1; M_MAX = 2000000000   # M 최소, 최대 정의
TH_MIN = 0; TH_MAX = 1000000000   # 떡 개별 높이 최소, 최대 정의


# 떡볶이 떡 자르는 클래스
class TteokCut:
    # 생성자
    def __init__(self):
        self.pas = -1   # 올바른 N, M 입력을 위한 변수
        self.N = None   # 떡 개수
        self.M = None   # 요청한 떡 길이
        self.th_list = None   # 떡 개별 높이를 담는 리스트

    # N, M 입력 메소드
    def input_data(self):
        n, m = list(map(int, input().split()))   # N, M 입력
        if (not isinstance(n, int)) or (not isinstance(m, int)): return -1   # N, M 중 하나라도 정수가 아닌 경우
        if n < N_MIN or n > N_MAX: return -1   # N이 최소, 최대 이외의 범위인 경우
        if m < M_MIN or m > M_MAX: return -1   # M이 최소, 최대 이외의 범위인 경우

        self.N = n   # 최종 N 값 저장
        self.M = m   # 최종 M 값 저장
        return 1   # 올바른 N, M 값이 입력된 경우 1 반환

    # 떡 개별 높이 입력 메소드
    def input_list(self):
        self.th_list = list(map(int, input().split()))   # 떡 개별 높이를 담는 리스트
        if sum(self.th_list) < self.M: return -1   # 총합이 M 미만인 경우
        for t in self.th_list:   # 떡 개별 높이 리스트 길이 만큼 반복
            if t < TH_MIN or t > TH_MAX: return -1   # 떡 개별 높이가 최소, 최대 이외의 범위인 경우

        # for i in self.__N:   # 떡 개별 높이 리스트 길이 만큼 반복
        #     self.__th_list[i] = [0 for _ in range(self.__th_list[i])]   # 떡 높이 만큼 리스트 생성
        return 1   # 올바른 떡 개별 높이가 입력된 경우 1 반환

    # 자른 떡 높이 총합 계산하는 메소드
    def sum_tteok(self, start, mid, end):
        cut_tteok = 0
        for i in range(self.N):
            if mid > end: continue
            cut_tteok += end - mid
        return cut_tteok

    def binary_search(self):
        start = 0   # 시작점
        end = max(self.th_list)   # 끝점
        mid = (start + end) // 2  # 중간점

        while start <= end:   # 이진탐색 스타트!
            sum = self.sum_tteok(start, mid, end)
            if sum > self.M:
                start = mid + 1
                mid = (start + end) // 2  # 중간점
            elif sum < self.M:
                end = mid - 1
                mid = (start + end) // 2  # 중간점
            elif sum == self.M:
                return mid

    # 프로그램 실행 메소드
    def run(self):
        # 올바른 N, M 값이 입력될 때까지 반복
        while self.pas <= -1:
            # os.system('cls')   # 화면 클리어
            self.pas = self.input_data()   # N, M 입력 메소드
            self.pas += self.input_list()  # 떡 개별 높이 입력 메소드
        h = self.binary_search()   # 이진탐색 수행
        print(h)


# main 함수
if __name__ == "__main__":
    tc = TteokCut()  # 객체 생성
    tc.run()  # 떡볶이 떡 자르기 프로그램 실행
    
# git test 