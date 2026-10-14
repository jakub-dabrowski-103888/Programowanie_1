#Zadanie 10 - wersja obiektowa



def wyznacz_ocene(punkty):
    if 0 <= punkty <= 49:
        return 2.0
    elif punkty <= 59:
        return 3.0
    elif punkty <= 69:
        return 3.5
    elif punkty <= 79:
        return 4.0
    elif punkty <= 89:
        return 4.5
    else:
        return 5.0

def uruchom():
    print("Zadanie-10")
    print()


    studenci_z_zaliczeniem = 0
    lista_studentow = []

    while True:
        try:
            liczba_studentow = int(input("Podaj liczbe studentow: "))
            if liczba_studentow > 0:
                break
            print("Liczba studentów musi być większa od zera\n")


        except ValueError:
            print("Błąd: Musisz podać liczbę całkowitą.\n")


    print()

    for i in range(1, liczba_studentow + 1):
        nazwisko = input(f"\nNazwisko studenta {i}: ").strip()

        while True:
            punkty = int(input("Punkty (0-100): "))

            if 0 <= punkty <= 100:
                break

            print("Nieprawidłowa liczba punktów. Sprobuj ponownie.")

        ocena = wyznacz_ocene(punkty)
        lista_studentow.append((nazwisko, punkty, ocena))

        if ocena >= 3.0:
            studenci_z_zaliczeniem += 1

    print("\nWyniki studentów:")

    for nazwisko, punkty, ocena in lista_studentow:
        print(f"{nazwisko} - {punkty} pkt - ocena {ocena:.1f}")

    print(f"\nLiczba studentów, którzy zaliczyli: {studenci_z_zaliczeniem}")


    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")