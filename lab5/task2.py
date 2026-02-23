numbers = [7, -2, 10, 4, 1]

summa = 0
max_elem = numbers[0]
min_elem = numbers[0]

# Обработка массива
for num in numbers:
    # Сумма
    summa += num
    
    # Максимум
    if num > max_elem:
        max_elem = num
        
    # Минимум
    if num < min_elem:
        min_elem = num

average = summa / len(numbers)

# Вывод результатов
print("Массив:", numbers)
print("Сумма элементов:", summa)
print("Максимальный элемент:", max_elem)
print("Минимальный элемент:", min_elem)
print("Среднее арифметическое:", average)
