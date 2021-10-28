s = input()
word = s[s.find('h'):s.rfind('h')+1]
anagram = word[::-1]
print(s[:s.find('h')] + anagram + s[s.rfind('h')+1:]) #записать предложение переставив символы от первого до последнего в обратном порядке