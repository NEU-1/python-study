num = int(input())
score = list(map(int, input().split()))

max_score = max(score)
average_score = (sum(score)*100/max_score)/num
print(average_score)