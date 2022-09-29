menu = 'Обменник'


def ecxachange():
    x = float(input('Сколько вы хотите обменять USD: '))
    y = 43.55
    print(x*y)


def ecxachange_ua():
    x = float(input('Сколько вы хотите обментья UAH: '))
    y = 43.55
    print((x/y))


def display_menu():
    print(f'Exchange: {menu}')
    print("""
1. Обменять доллары
2. Обменять гривны
3. Выход
""")


while True:
    display_menu()
    x = input("Выберете пункт меню (1-3): ")
    if x == '1':
        print(f'UAH: {ecxachange()}')
    elif x == '2':
        print(f'USD: {ecxachange_ua()}')
    elif x == '3':
        print('Good day')
        exit(0)





