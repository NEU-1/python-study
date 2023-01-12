a = input()

b = len(a)

line_0 = '0'*((b-1)//2) +'1'+'0'*((b-1)//2)

rule = {'111':'0','110':'1','101':'0','100':'1','011':'1','010':'0','001':'1','000':'0'}

print(line_0)

while line_0[1] == '0':
    line_n = line_0
    line_0 = '0' * b
    
    for i in range(1,b-1):
        line_0 = line_0[:i] + rule[line_n[i-1:i+2]] + line_0[i+1:]
    print(line_0)
        
