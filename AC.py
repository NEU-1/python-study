T = int(input())
for t in range(T):
    word = list(input())
    num_max = int(input())
    case = input()[1:-1].split(',')
    r = 1
    num_min = 0
    # case = map(int, case)
    # print(type(case))
    if word.count('D') > num_max:
        print('error')
        continue
    else:
        for w in word:
            if w == 'R':
                r *= -1
            elif w == 'D':
                if r == 1:
                    num_min += r
                else:
                    num_max += r
        case = case[num_min:num_max]
        case = case[::r]

        if num_max == 0:
            print(case)
        else:
            print('[',end='')
            print(",".join(case), end='')
            print(']')




from sys import stdin
input = stdin.readline

def solve():

    for _ in range(int(input())):
        # 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
        p = [*map(len, input()[:-1].replace('RR', '').split('R'))]

        n = int(input())
        arr = input()[1:-2].split(',')
        # [left, right) 가 출력된다
        left, right = sum(p[::2]), n - sum(p[1::2])

        if left <= right:
            # len(p) % 2 == 1 인 경우 왼쪽에서 오른쪽 방향
            arr = arr[left:right] if len(p) % 2 else reversed(arr[left:right])
            print(f"[{','.join(arr)}]")
        else:
            print('error')

if __name__ == '__main__':
    solve()