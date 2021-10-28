s = input()
first_place = s.find ('h')
last_place = s.rfind ('h')
print (s[:first_place] + s[last_place+1:]) #найти первый и последний индекс и удалить символы между ними