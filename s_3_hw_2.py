# Задание 2
# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5,5]

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

print(find_duplicates(lst))
