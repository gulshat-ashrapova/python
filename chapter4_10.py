n = int(input())
for i in range (1, n+1):
    for m in range (1, i+1):
        print (m, sep='', end='')
    print()  # лесенка из чисел от 1 до n     