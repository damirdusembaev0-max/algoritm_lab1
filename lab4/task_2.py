while True:
    try:
        x = int(input("Введите число: "))
        if x > 100:
            print("Введено число больше 100:", x)
            break
        else:
            print("Число должно быть больше 100")
    except ValueError:
        print("Введите корректное число!")
