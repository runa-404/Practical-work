print('----------------------------------------------------------------------')
print('~Темний ліс~')
print('----------------------------------------------------------------------')
print("Ти — відважний мандрівник, що опинився на роздоріжжі в темному лісі.")
print("Обери шлях: 1 — стежка ліворуч, 2 — стежка праворуч")

vubir1 = input("Введи 1 або 2: ")

if vubir1 == "1":
    print("\nТи виходиш до широкої ріки. Води бурхливі.")
    print("a) Пірнаю та пливу попри течію.")
    print("b) Будую пліт із підручних матеріалів.")
    vubir2 = input("Введи a або b: ")

    if vubir2 == "a":
        print("\nТечія заносить тебе під водоспад. Ти не встигаєш виплисти — ~Game Over~")
    elif vubir2 == "b":
        print("\nТвій пліт міцний, і ти благополучно переправляєшся на інший берег.\nПопереду — скарб! Ти багатий!")
    else:
        print("\nНевірний вибір. Ріка вирішила, що ти нецікавий глядач — ~Game Over~")

elif vubir1 == "2":
    print("\nСтежка приводить до темної печери.")
    print("a) Заходжу всередину.")
    print("b) Минаю печеру й іду далі стежкою.")
    vubir3 = input("Введи a або b: ")

    if vubir3 == "a":
        print("\nУ печері — сплячий дракон!")
        print("1) Битися з драконом.")
        print("2) Спішно тікати назад.")
        vubir4 = input("Введи 1 або 2: ")

        if vubir4 == "1":
            print("\nУдача на твоєму боці: дракон не встиг прокинутися й програв бій. Ти здобув золото — Ти виграв!")
        elif vubir4 == "2":
            print("\nДракон прокидається й вловлює твій страхливий відхід. Тебе наздоганяють — ~Game Over~")
        else:
            print("\nНевідомий код дії. Дракон прокинувся й зібрався на вечерю — ~Game Over~")

    elif vubir3 == "b":
        print("\nТи віддаляєшся від печери, але заблукав у темному лісі.\nГолод і спрага беруть своє — ~Game Over~")
    else:
        print("\nНевірний вибір. Ліс вирішив, що ти не заслуговуєш на подорож — ~Game Over~")

else:
    print("\nТи вагаєшся занадто довго. Ліс замкнув тебе в обійми — ~Game Over~")