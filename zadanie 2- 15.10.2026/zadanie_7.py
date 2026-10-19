


magazyn = {
    "Mysz": 5,
    "Klawiatura": 3,
    "Monitor": 2
}






while True:
    print("\n1. Stan magazynu")
    print("2. Przyjecie towaru")
    print("3. Wydanie towaru")
    print("0. Zakoncz")

    try:
        opcja = int(input("Wybierz opcje: "))
    except ValueError:
        print("Blad: podaj liczbe calkowita.")
        continue

    if opcja == 1:
        for produkt in magazyn:
            print(f"{produkt}: {magazyn[produkt]} szt.")

    elif opcja == 2:
        nazwa = input("Nazwa produktu: ").strip()

        if nazwa == "":
            print("Blad: nie podales nazwy produktu.")
            continue

        while True:
            try:
                ilosc = int(input("Liczba sztuk: "))

                if ilosc > 0:
                    break

                print("Liczba sztuk musi byc wieksza od zera.")

            except ValueError:
                print("Blad: podaj liczbe calkowita.")

        if nazwa in magazyn:
            magazyn[nazwa] += ilosc
        else:
            magazyn[nazwa] = ilosc

        print("Zaktualizowano stan produktu.")

    elif opcja == 3:
        nazwa = input("Nazwa produktu: ").strip()

        if nazwa not in magazyn:
            print("Blad: produkt nie znajduje sie w magazynie.")
            continue

        while True:
            try:
                ilosc = int(input("Liczba sztuk: "))

                if ilosc > 0:
                    break

                print("Liczba sztuk musi byc wieksza od zera.")

            except ValueError:
                print("Blad: podaj liczbe calkowita.")

        if magazyn[nazwa] >= ilosc:
            magazyn[nazwa] -= ilosc
            print(f"Wydano {ilosc} szt.")
        else:
            print("Blad: niewystarczajaca liczba sztuk w magazynie.")

    elif opcja == 0:
        print("Do widzenia!")
        break

    else:
        print("Blad: nieprawidlowa opcja.")