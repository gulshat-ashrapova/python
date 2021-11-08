number = int(input()) #суммировать числа пока в последовательности не появится 0
sum = 0
while number != 0:
    sum += number
    number = int(input())
print (sum)