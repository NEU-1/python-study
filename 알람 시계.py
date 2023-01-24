hour, minute = list(map(int, input().split()))

if minute < 45:
    hour -= 1
    minute += 60
    if hour == -1:
        hour += 24
print(f'{hour} {minute-45}')

H , M = map(int, input().split())
total = H * 60 + M - 45
if total < 0:
    total += 60 *24
H = total // 60
M = total % 60
print(H, M)