
qube = [list(map(int, input().split())) for i in range(9)]
y, x = map(int, input().split())
   
sub_y, sub_x = (y//3)*3, (x//3)*3
print(*list(qube[sub_y + i // 3][sub_x + i % 3] for i in range(9)))
  
  
sub_y, sub_x = (y//3)*3, (x//3)*3
print(*list(qube[sub_y+i][sub_x+j] for i in range(3) for j in range(3)))


'''
qube
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

'''