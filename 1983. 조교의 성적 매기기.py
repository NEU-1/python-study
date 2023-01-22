import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    # print(N,K)
    student = []
    count = 0
    count_no = 0    
    for n in range(N): # 학생별 평균값 대입
        three = list(map(int, input().split()))
        student.append(float(three[0]*0.35 + three[1]*0.45 + three[2]*0.2))
        three = []
    student_K = student[K-1] # 상위 점수 학생수 체크
    # print(student_K)
    student.sort()
    # print(student)
    num = N-student.index(student_K)-1

    rank = (num//(N/10))
    if rank == 0:
        clear = 'A+'
    elif rank == 1:
        clear = 'A0'
    elif rank == 2:
        clear = 'A-'
    elif rank == 3:
        clear = 'B+'
    elif rank == 4:
        clear = 'B0'
    elif rank == 5:
        clear = 'B-'
    elif rank == 6:
        clear = 'C+'
    elif rank == 7:
        clear = 'C0'
    elif rank == 8:
        clear = 'C-'
    else:
        clear = 'D0'
    print(f'#{t} {clear}')
    

for t in range(int(input())):
    N,K=map(int,input().split())
    r=[[*map(int,input().split())]for _ in range(N)]
    k=r[K-1]
    r.sort(key=lambda x:.35*x[0]+.45*x[1]+.2*x[2])
    print(f"#{t+1} {['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+'][r.index(k)//(N//10)]}")