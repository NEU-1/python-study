def dfs(num, a):
    global mx, mn
    if num == n + 1:
        mx = max(mx, a)
        mn = min(mn, a)
        return

    for i in range(10):
        if visited[i]:
            continue

        if num == 0 or check(a[-1], str(i), ques[num - 1]):
            visited[i] = True
            dfs(num + 1, a + str(i))
            visited[i] = False

def check(a, b, ques):
    if ques == '<':
        return a < b
    else:
        return a > b

n = int(input())
ques = input().split()
visited = [False] * 10
mx = ''
mn = '9999999999'
dfs(0, '')

print(mx)
print(mn)
