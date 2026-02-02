score = int(input("Введите число от 1 до 100: "))

if score < 1 or score > 100:
    print("Ошибка: число должно быть в диапазоне от 1 до 100")
elif score >= 90:
    print("Оценка: A")
elif score >= 75:
    print("Оценка: B")
elif score >= 60:
    print("Оценка: C")
else:
    print("Оценка: D")