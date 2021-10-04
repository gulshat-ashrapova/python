lesson = int(input())
if lesson % 2 == 0:
    hour_end_of_lesson = 9 + ((45 * lesson + 5 * (lesson/2) + 15 * (lesson/2 -1)) //60)
    min_end_of_lesson = (45 * lesson + 5 * (lesson/2) + 15 * (lesson/2 -1)) %60
else:
    hour_end_of_lesson = 9 + ((45 * lesson + 5 * (lesson/2) + 15 * (lesson/2 -1)) //60)
    min_end_of_lesson = (45 * lesson + 5 * int(lesson/2) + 15 * int(lesson/2)) %60
print (hour_end_of_lesson, min_end_of_lesson)