#Zadanie 9

import os


def uruchom():
    print("Zadanie-9")
    print()
    poczatek_zakresu=0

    koniec_zakresu=0

    parzyste=0


    while True:
        try:

            poczatek_zakresu = int(input("Podaj poczatek zakresu : "))

            if poczatek_zakresu <= 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Błąd: zakres musi byc wiekszy niz zero. Sprobuj ponownie.\n")
                continue

            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")


    while True:
        try:

            koniec_zakresu = int(input("Podaj koniec zakresu : "))

            if koniec_zakresu <= 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Błąd: zakres musi byc wiekszy niz zero. Sprobuj ponownie.\n")
                continue

            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")



    for i in range( poczatek_zakresu, koniec_zakresu+1 ):
        if i % 2==0:
            print(f"{i} - Parzysta")
            parzyste+=1
        else:
            print(f"{i} - Nieparzysta")

    print(f"\nLiczba liczb parzystych: {parzyste}")

    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")