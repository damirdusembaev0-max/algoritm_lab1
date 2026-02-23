# Ввод количества элементов
n = int(input("(n > 5):"))

# Проверка корректности ввода
while n <= 0:
    print(" 5.")
    n = int(input("(n > 5): "))

# Создание пустого массива
numbers = [1]

# Ввод элементов массива
for i in range(n):
    num = int(input(f"Введите элемент {i + 1}: "))
    numbers.append(num)

# Вывод массива
print("Полученный массив:", numbers)