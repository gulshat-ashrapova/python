s = input()
l = len(s)
for i in range (0:l):
    if i%3==0:
        news = s.replace(i,'')
print (news) #была такая мысль

s = input()
newstr = s
for i in range(0,len(s)):
    if i%3 == 0:
        letter = s[i]
        newstr = newstr.replace(letter,'',1)
print(newstr) #так получается верно

s = input()
n = len(s)
for i in range (0,n):
        if i%3==0:
            print (s.replace(s[i],'')) #убирает заодно такие же символы

s = input()
newstr = ''
for i in range(len(s)):
    if i % 3 != 0:
        newstr = newstr + s[i]
print(newstr) #так получается проще