n=int(input())
dp=[0]*(n+3)
dp[1],dp[2],dp[3]=0,1,1
for i in range(4,n+1):
    if i%2==0 and i%3==0:
        dp[i]=min(dp[i//3],dp[i//2],dp[i-1])+1
    elif i%3==0:
        dp[i] = min(dp[i // 3],dp[i-1]) + 1
    elif i%2==0:
        dp[i] = min(dp[i // 2],dp[i-1]) + 1
    else:
        dp[i]=dp[i-1]+1
print(dp[n])




import sys
d = {1: 0, 2: 1}
def s(n: int) -> int:
    if n in d:
        return d[n]
    t = 1 + min(s(n // 3) + n % 3, s(n // 2) + n % 2)
    d[n] = t
    return t
print(s(int(sys.stdin.readline())))