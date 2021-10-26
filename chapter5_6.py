s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print (-2)
elif s.count('f') >= 2:    
    first = s.find('f') 
    print (s.find ('f', first+1)) #найти второе положение символа в строке