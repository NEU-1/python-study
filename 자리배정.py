def deep(num):
    if num == 0:
        return 0
    return deep(num-1)+num*4

x, y = map(int,input().split())
ticket = int(input())

if x*y < ticket:
    print(0)
else:
    # check = 1
    # inside = 0
    # while check < ticket:
    #     inside += 1
    #     if x*2+y*2-deep(inside) <= 0:
    #         check += x*2+y*2-deep(inside)
    #         break
    #     else:
    #         check += x*2+y*2-deep(inside)
    #     # print(check)
    #     # print(inside)


    # X = inside + 1
    # Y = inside + 1
    # go = ticket - check + x*2+y*2-deep(inside)
    # print(X, Y)
    # # print(go)

    # if go <= y-inside:
    #     Y += go
    # else:
    #     go -= y-inside
    #     Y += y-inside
    #     # print(X, Y)
    #     if go <= x-inside:
    #         X += go
    #     else:
    #         go -= x-inside
    #         X += x-inside
    #         # print(X, Y)
    #         if go <= y-inside:
    #             Y -= go
    #         else:
    #             go -= y-inside
    #             Y -= y-inside
    #             # print(X, Y)
    #             if go <= x-inside-1:
    #                 X -= go

    # print(X, Y)
