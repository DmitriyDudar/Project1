from colorama import Back, Fore, Style

blok = True

while blok:
    print(Fore.BLUE)
    numix1 = input("Введите ваше ФИО: ")
    numix2 = input("Введите ваш год рождения: ")
    numix3 = input("Введите вашу почту: ")
    print(Fore.LIGHTCYAN_EX)
    x = input(f"Ваше ФИО: {numix1} \nВаш год рождения: {numix2} \nВаша почта: {numix3} \nВерно? 'y', \'n': ")

    if x == "y":
        print(Fore.CYAN)
        mls = input("Желаете записать данные в файл 'text.txt'? \'y' \'n': ")
        if mls == "y":
            files = open('text.txt', 'a')
            mripe = files.write(f"ФИО: {numix1} \nГод рождения: {numix2} \nПочта: {numix3}\n\n")
            files.close()
            quit()
        else:
            quit()
    else:
        blok