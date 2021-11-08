number_of_bigger = -1
num = int(input())
previous_num = 0
while num != 0:
    if num > previous_num:
        number_of_bigger += 1
    previous_num = num    
    num = int(input())    
print (number_of_bigger)   # посчитать количество элеметов больше чем предыдущих