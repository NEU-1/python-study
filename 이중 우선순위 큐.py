import heapq
import sys
input = sys.stdin.readline

t = int(input())  # 테스트 케이스 개수 입력
for _ in range(t):
    n = int(input())  # 명령의 개수 입력
    mn_heap = []  # 최소 힙
    mx_heap = []  # 최대 힙
    visited = [False] * n  # 삭제된 원소 확인을 위한 리스트
    for i in range(n):
        word, num = input().split()  # 명령 입력
        num = int(num)
        if word == 'I':  # 삽입 명령일 경우
            heapq.heappush(mn_heap, (num, i))  # 최소 힙에 삽입
            heapq.heappush(mx_heap, (-num, i))  # 최대 힙에 삽입
        elif word == 'D':  # 삭제 명령일 경우
            if len(mn_heap) == 0:  # 힙이 비어있는 경우
                continue
            if num == 1:  # 최댓값 삭제 명령일 경우
                while mx_heap and visited[mx_heap[0][1]]:  # 삭제된 원소는 건너뛴다.
                    heapq.heappop(mx_heap)
                if mx_heap:  # 최댓값 삭제
                    visited[mx_heap[0][1]] = True  # 삭제된 원소 표시
                    heapq.heappop(mx_heap)
            elif num == -1:  # 최솟값 삭제 명령일 경우
                while mn_heap and visited[mn_heap[0][1]]:  # 삭제된 원소는 건너뛴다.
                    heapq.heappop(mn_heap)
                if mn_heap:  # 최솟값 삭제
                    visited[mn_heap[0][1]] = True  # 삭제된 원소 표시
                    heapq.heappop(mn_heap)
    while mx_heap and visited[mx_heap[0][1]]:  # 삭제된 원소는 건너뛴다.
        heapq.heappop(mx_heap)
    while mn_heap and visited[mn_heap[0][1]]:  # 삭제된 원소는 건너뛴다.
        heapq.heappop(mn_heap)
    if len(mn_heap) == 0:  # 힙이 비어있는 경우
        print("EMPTY")
    else:
        print(-mx_heap[0][0], mn_heap[0][0])  # 최댓값과 최솟값 출력
