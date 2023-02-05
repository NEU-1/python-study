for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = list(map(int,input().split()))

    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')
    elif p1 == x2 or p2 == x1:
        if y1 == q2 or y2 == q1:
            print('c')
        else:
            print('b')
    elif y1 == q2 or y2 == q1:
        print('b')
    else:
        print('a')

    #----------------------------------------
    # square_1 = set()
    # square_2 = set()
    # for y1 in range(number[1]*2, number[3]*2+1):
    #     square_1.add((y1, number[0]*2))
    #     square_1.add((y1, number[2]*2))
    # for y2 in range(number[5]*2, number[7]*2+1):
    #     square_2.add((y2, number[4]*2))
    #     square_2.add((y2, number[6]*2))
    
    # for x1 in range(number[0]*2, number[2]*2+1):
    #     square_1.add((number[1]*2, x1))
    #     square_1.add((number[3]*2, x1))
    # for x2 in range(number[4]*2, number[6]*2+1):
    #     square_2.add((number[5]*2, x2))
    #     square_2.add((number[7]*2, x2))
    # save = square_1 & square_2
    # print(square_1, square_2)
    # print(save)
    #----------------------------------------
    # square_1 = [(y1, x) for y1 in range(number[0], number[2]+1) for x in range(number[1], number[3]+1)]
    # square_2 = [(y1, x) for y1 in range(number[4], number[6]+1) for x in range(number[5], number[7]+1)]

    # # print(square_1)
    # s1 = set(square_1)
    # s2 = set(square_2)
    # # print(s1, s2)
    # save = s1 & s2
    # save_x = []
    # save_y = []
    # for X,Y in save:
    #     save_x.append(X)
    #     save_y.append(Y)
    # # print(save)
    # # print(len(save))
    # if len(save) == 0:
    #     print('d')
    # elif len(save) == 1:
    #     print('c')
    # elif len(save) > 1:
    #     if max(save_x) == min(save_x) or max(save_y) == min(save_y):
    #         print('b')
    #     else:
    #         print('a')