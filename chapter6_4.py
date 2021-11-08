x = int (input())
y = int (input())
while x <= y:
    x = x + x / 100
    print (x) # почему цикл не прерывается?

x = int (input())
y = int (input())
res = 1
while x < y:
    x *= 1.1
    res+=1
print (res) #каждое следующее число на 10% больше
