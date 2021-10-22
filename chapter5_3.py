s = str(input())
l = int (len(s)/2)
m = l + len(s) % 2
print (s[m:] + s[:m])