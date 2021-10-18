P = int(input())
X = int(input())
Y = int(input())
itogo = int ((X * 100 + Y) * P / 100 + (X * 100 + Y))
rubli = itogo // 100
kopeiki = itogo % 100
print (int(rubli), int(kopeiki))