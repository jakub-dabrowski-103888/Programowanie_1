#Zadanie 8
import os


def uruchom():
    print("Zadanie-8")
    print()
    wysokosc=0


    while True:
        try:

            wysokosc = int(input("Podaj wysokosc choinki : "))

            if wysokosc <= 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Błąd: wysokosc choinki musi byc wieksza niz zero. Sprobuj ponownie.\n")
                continue

            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")

    print()

    for i in range(wysokosc):
        spacje = " " * (wysokosc - 1 - i)
        gwiazdki = "*" * (2 * i + 1)
        print(spacje + gwiazdki)

    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")