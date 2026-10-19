zadania = []

print("Menu")
while True:
    print("\n1. Dodaj zadanie")
    print("2. Wyswietl zadania")
    print("3. Usun zadanie")
    print("4. Liczba zadan")
    print("0. Zakoncz")

    try:
        opcja = int(input("Wybierz opcje: "))
    except ValueError:
        print("Blad: podaj liczbe calkowita.")
        continue

    if opcja == 1:
        zadanie = input("Podaj zadanie: ")

        if zadanie == "":
            print("Blad: nie podales nazwy zadania.")
        else:
            zadania.append(zadanie)

    elif opcja == 2:
        if len(zadania) == 0:
            print("Brak zadan.")
        else:
            for i in range(len(zadania)):
                print(f"{i + 1}. {zadania[i]}")

    elif opcja == 3:
        if len(zadania) == 0:
            print("Brak zadan.")
        else:
            try:
                numer = int(input("Podaj numer zadania: "))

                if 1 <= numer <= len(zadania):
                    zadania.pop(numer - 1)
                    print("Zadanie usuniete.")
                else:
                    print("Blad: nieprawidlowy numer zadania.")

            except ValueError:
                print("Blad: podaj liczbe calkowita.")

    elif opcja == 4:
        print(f"Liczba zadan: {len(zadania)}")

    elif opcja == 0:
        print("Do widzenia!")
        break

    else:
        print("Blad: nieprawidlowa opcja.")