T = int(input()) #첫 값
n= int(input()) #자연수 수
num_1 = list(map(int,input().split())) # 목록
d = num_1[n-1]
b = [d] #저장소
c = [n] #위치 저장소

for l in c:
    for i in range(1,n+1):
        if num_1[n-i-1]<num_1[n-i] and num_1[n-i]>d:
            b.append(num_1[n-i])
            c.append(n-i)
            d = num_1[n-i]
    e = c[i]-c[i+1]
    f = e * b[i]
    print(f)
