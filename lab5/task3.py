numbers = [5, -3, 8, 0, -2, 7, -1]

# Счётчики
positive_count = 0
negative_count = 0
even_count = 0

# Обход массива
for num in numbers:
    
    # Проверка на положительные
    if num > 0:
        positive_count += 1
    
    # Проверка на отрицательные
    if num < 0:
        negative_count += 1
    
    # Проверка на чётность
    if num % 2 == 0:
        even_count += 1

# Вывод результатов
print("Массив:", numbers)
print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)
print("Количество чётных элементов:", even_count)
