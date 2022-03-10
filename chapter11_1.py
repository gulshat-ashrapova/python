# Задача «Номер появления слова»
#
# В единственной строке записан текст.
# Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
#
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.


words = input().split() #разбили на слова
frequencies = dict()
answer = []
for i in words:
    if i in frequencies:
        frequencies[i] = frequencies.get(i) + 1
    else:
        frequencies[i] = 0
    answer.append(frequencies[i])

print(' '.join([str(i) for i in answer]))