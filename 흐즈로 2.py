n = int(input())
a = list(map(int, input().split()))

# 내림차순으로 정렬
a.sort(reverse=True)

# 2^k 꼴의 수 중에서 큰 수부터 차례로 사용
ans = 0
used = set()
for x in a:
    if x in used:
        continue
    k = 0
    while x > 1:
        x //= 2
        k += 1
    if k not in used:
        ans += 2 ** k
        used.add(k)
    print(ans)

print(ans)
