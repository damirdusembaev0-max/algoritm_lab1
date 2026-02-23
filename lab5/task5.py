n = int(input("10: "))

if n < 2:
    print("Ошибка! В массиве должно быть минимум 2 элемента.")
else:
    numbers = []
    
  
    for i in range(n):
        num = int(input(f"Введите элемент {i + 1}: "))
        numbers.append(num)

    print("Массив:", numbers)

    
    max1 = numbers[0]
    max2 = None

    for num in numbers[1:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num != max1:  
            if max2 is None or num > max2:
                max2 = num

   
    if max2 is None:
        print("Второго по величине элемента нет (все элементы равны).")
    else:
        print("Второй по величине элемент:", max2)