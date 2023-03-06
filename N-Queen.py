# def queen(chess, y, size):
#     if y == size:
#         return 1
#
#     save = 0
#     for x in range(size):
#         if check(chess, y, x, size):
#             chess[y][x] = 1
#             save += queen(chess, y+1, size)
#             chess[y][x] = 0
#     return save
#
# def check(chess, y, x, size):
#     for y_ in range(y):
#         if chess[y_][x] == 1:
#             return False
#
#     for y_, x_ in zip(range(y, -1, -1), range(x, -1, -1)):
#         if chess[y_][x_] == 1:
#             return False
#
#     for y_, x_ in zip(range(y, -1, -1), range(x, size)):
#         if chess[y_][x_] == 1:
#             return False
#
#     return True
#
# size = int(input())
# chess = [[0]*size for _ in range(size)]
# print(queen(chess, 0, size))
#
#


def queen(y):
    if y == size:
        return 1

    count = 0
    for x in range(size):
        chess[y] = x
        if check(y):
            count += queen(y+1)
    return count

def check(y):
    for y_ in range(y):
        if chess[y] == chess[y_] or abs(chess[y] - chess[y_]) == y-y_:
            return False
    return True


size = int(input())
chess = [0]*size
y = 0
print(queen(y))
# print(chess)
