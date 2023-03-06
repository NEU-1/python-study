# # 소수 리스트 뽑고
# # 뒤에부터 순회하면서 각각 더해서 입력값이 되면 YES
# # 끝까지 했는데 안되면 NO

# import bisect

# def prime_list(num):
#     prime = []
#     check = [True]*(num+1)
#     check[True], check[1] = False, False
#     for n in range(1, int(num**0.5)+1):
#         if check[n] == True:
#             check[n*n::n] = [False] * ((num - n*n) // n + 1)
#     # for i in range(2, num+1):
#     #     if check[i] == True:
#     #         prime.append(i)
#     # return prime
#     return [i for i in range(2, num+1) if check[i] == True]

# def musbi(a, b, prime):
#     num = a + b
#     start = 0
#     end = len(prime)-1
#     while start < end:
#         if prime[start] + prime[end] == num:
#             return 'YES'
#         elif prime[start] + prime[end] < num:
#             start += 1
#         else:
#             end -= 1
#     # for n in range(len(prime)):
#     #     if prime[n] >= num:
#     #         break
#     #     else:
#     #         m = bisect.bisect_left(prime, num - prime[n])
#     #         if m < n and prime[n] + prime[m] == num:
#     #             return 'YES'
#     return 'NO'





# T = int(sys.stdin.readline())
# save = []
# for _ in range(T):
#     짝, 꿍 = map(int,sys.stdin.readline().split())
#     save.append((짝,꿍))

# max_team = max([(짝+꿍) for 짝, 꿍 in save])
# prime = prime_list(max_team)
# for 짝,꿍 in save:    
#     print(musbi(짝, 꿍, prime))
  
# import sys

# def list_prime():
#     a = 2000001
#     check = [True]*a
#     check[0], check[1] = False, False
#     for i in range(2, int(a**0.5)+1):
#         if check[i] == True:
#             for k in range(i*2, a, i):
#                 check[k] = False
#     return [j for j in range(2, a) if check[j]]

# def goldbah(num, prime):
#     num_2 = num**2
#     for i in range(0, len(prime)):
#         if prime[i] > num_2: 
#             break
#         if num % prime[i] == 0:
#             if prime.count(num-prime[i]) > 0:
#                 return 'NO'
#     return 'YES'

# T = int(sys.stdin.readline())
# save = []
# for _ in range(T):
#     a, b = map(int,sys.stdin.readline().split())
#     save.append((a+b))

# prime = list_prime()
# for num in save:    
#     if num < 4:
#         print('NO')
#     elif num % 2 == 0:
#         print('YES')
#     else:
#         num -= 2
#         print(goldbah(num, prime))


# 수 받아서 합쳐 놓고
# 범위값의 제곱근에 해당하는 소수 리스트 뽑아놓고
# 4 미만은 no 4 이상은 짝수는 yes 나머진 판별
# 합친값이 그보다 작은 수로 나눠지면 소수 아님
import sys

def prime():
    a = (2*(10**6))+1
    check = [0] * a
    check[0], check[1] = 1, 1
    for i in range(2, int(a**0.5)+1):
        if check[i] == 0:
            for j in range(i*2, a, i):
                check[j] = 1
    return [z for z in range(2, a) if check[z] == 0]

def goldbah(num, prime):
    num_2 = num**2
    for p in prime:
        if p > num_2:
            break
        if num % p == 0 and num != p:
            return 'NO'
    return'YES'
        


T = int(sys.stdin.readline())
save = []
for _ in range(T):
    a, b = map(int,sys.stdin.readline().split())
    save.append(a+b)

prime = prime()

for s in save:
    if s < 4:
        print('NO')
    elif s % 2 == 0:
        print('YES')
    else:
        s -= 2
        print(goldbah(s, prime))

