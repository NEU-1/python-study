t = int(input())
i = 1


while i <= t:

    num = input()

    num_list = num.split()

    len_num = len(num_list)
    

    i_num_list = map(int,num_list)


    sum_num = sum(i_num_list)/len_num

    sum_num = round(sum_num)
    
    print(f'#{i} {sum_num}')

    i=i+1
    


