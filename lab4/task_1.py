while True:
    try:
        x = int(input("Введите целое число: "))
        if x > 0:
            print("Корректное число:", x)
            break
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Пожалуйста, введите именно целое число.")
