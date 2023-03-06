
def team(num, save, s, start):
    # print(save)
    if len(start) == num//2:
        # print(start)
        link = list(set(range(num)) - set(start))
        # print(start, link)
        save = min(abs(check(start) - check(link)), save)
        # print(check(start), check(link))
        if save == 0:
            return save
        return save

    for n in range(s, num):
        start.append(n)
        save = team(num, save, n+1, start)
        start.pop()
    return save

def check(team):
    hap = 0
    for t in range(len(team)-1):
        for e in range(t+1, len(team)):
            # print(team)
            hap += stat[team[t]][team[e]]
    return hap




num = int(input())
stat = [list(map(int,input().split())) for _ in range(num)]

for y in range(num):
    for x in range(num):
        if x > y:
            stat[y][x] += stat[x][y]
        elif x < y:
            stat[y][x] = 0

# print(stat)
save = 999
start = []

save = team(num, save, 0, start)

print(save)







import sys
from itertools import combinations as cb

# 입력받은 인원 수의 절반을 계산
N = int(sys.stdin.readline()) // 2

# 입력받은 능력치를 이용하여 새로운 능력치를 계산
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]

# 모든 능력치의 합을 계산
allstat = sum(newstat) // 2

# N명의 팀을 뽑는 모든 경우에 대해 최소값을 구함
mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))

# 최소값 출력
print(mins)
