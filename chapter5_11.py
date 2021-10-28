s = input()
change = s[s.find('h')+1:s.rfind('h')]
first_part = s[:s.find('h')+1]
mid_part = change.replace('h','H')
last_part = s[s.rfind('h'):]
print(first_part + mid_part + last_part) #заменить h на H внутри строки без первого и последнего вхождения