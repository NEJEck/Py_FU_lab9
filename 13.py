"""
Задание 13. Частотный анализ
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по
убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
Указание.
После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота
встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет
сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны —то по второму. Это
почти то, что требуется в задаче."""
from collections import Counter

with open("input13.txt") as f:
    content = f.readlines()

words = []
for line in content:
    line = list(line.split())
    words.extend(line)

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))
