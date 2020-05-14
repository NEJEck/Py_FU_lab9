"""
Задание 12. Самое частое слово
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
Формат ввода
Вводится текст.
Формат вывода
Выведите ответ на задачу.
"""
counter = {}
line = input().split()
for word in line:
    counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
