import sys
from collections import Counter
num = int(int(sys.stdin.readline()))
num_list = []
for n in range(num):
    num_list.append(int(int(sys.stdin.readline())))
num_list.sort()

sum_num = round(sum(num_list)/num)
print(sum_num)

center_num = num_list[(num-1)//2]
print(center_num)

list_two = Counter(num_list).most_common(2)
if len(list_two) > 1:
    if list_two[0][1] == list_two[1][1]:
        print(list_two[1][0])
    else:
        print(list_two[0][0])
else:
    print(list_two[0][0])

range_num = num_list[-1]-num_list[0]
print(range_num)

# 하... 카운트 모스트...



import sys
input = sys.stdin.readline
cnt = int(input())
nums = [0] * 8001
for i in range(cnt):
    nums[int(input()) + 4000] += 1
avg = 0
num_count = 0; center = 4001
min_num = 4001; max_num = -4001
for i in range(8001):
    if nums[i] != 0:
        avg += (i - 4000) * nums[i]
        num_count += nums[i]
        if center == 4001 and num_count >= cnt/2:
            center = i - 4000
        if min_num > i - 4000:
            min_num = i - 4000
        if max_num < i - 4000:
            max_num = i - 4000
max_count = max(nums)
max_count_num = nums.index(max_count) - 4000
nums[max_count_num + 4000] = 0
if max(nums) == max_count:
    max_count_num = nums.index(max(nums)) - 4000
print(round(avg/cnt))
print(center)
print(max_count_num)
print(max_num - min_num)