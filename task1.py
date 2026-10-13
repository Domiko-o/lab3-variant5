try:
    minutes = int(input("Введите количество минут: "))
    seconds = int(input("Введите количество секунд: "))

    if minutes < 0:
        print("Ошибка: количество минут не может быть отрицательным!")
    elif seconds < 0 or seconds >= 60:
        print("Ошибка: количество секунд должно быть в диапазоне [0; 59]!")
    else:
        total = minutes * 60 + seconds
        print(f"{minutes} мин {seconds} сек = {total} сек")
except ValueError:
    print("Ошибка: необходимо ввести целые числа!")