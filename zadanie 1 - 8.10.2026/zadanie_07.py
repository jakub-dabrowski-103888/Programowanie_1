#Zadanie 7

import os

def uruchom():
    print("Zadanie-7")
    print()

    oszczednosci=0
    kwota_odkladana=0
    ilosc_tygodni=0

    while True:
        try:

            kwota_odkladana = int(input("ile odkladasz tygodniowo? : "))

            if kwota_odkladana < 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Błąd: Kwota oszczędności nie może być ujemna. Sprobuj ponownie.\n")
                continue

            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")

    while True:
        try:

            kwota_odkladana = int(input("Przez ile tygodni? : "))

            if ilosc_tygodni <= 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Błąd: Liczba tygodni musi być wieksza niz zero. Sprobuj ponownie.\n")
                continue

            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")

    print()

    for tydzien in range(1, ilosc_tygodni + 1):
        oszczednosci += kwota_odkladana
        print(f"Tydzien {tydzien}: {oszczednosci} zl")

    print()
    print(f"Laczne oszczednosci: {oszczednosci} zl")

    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")