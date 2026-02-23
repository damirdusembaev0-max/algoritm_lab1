numbers = [12, 5, 8, 21, 7]

print("Массив:", numbers)

# Ввод числа для поиска
target = int(input("5 : "))

# Переменная для хранения индекса
found_index = -1

# Линейный поиск
for i in range(len(numbers)):
    if numbers[i] == target:
        found_index = i
        break   # прекращаем поиск, если нашли

# Вывод результата
if found_index != -1:
    print("Число найдено! Индекс:", found_index)
else:
    print("Число в массиве не найдено.")
