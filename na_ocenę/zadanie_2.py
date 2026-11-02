
print("Zadanie 2 \n")

menu_opcja=99

rejestr = []

while True:
    print("\n========== Kalkulator  ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("7. Rejest dzialan na kalkulatorze")
    print("0. Zakoncz")
    print("=======================================")

    try:
        menu_opcja = int(input("Wybierz opcje: "))
    except ValueError:
        print("Blad: podaj liczbe calkowita.")
        continue

    if menu_opcja == 1:
        try:
            liczba_1 = float(input("Pierwsza liczba: "))
            liczba_2 = float(input("Druga liczba: "))

        except ValueError:
            print("Blad: podaj prawidlowa liczbe.")
            continue

        wynik = liczba_1 + liczba_2
        dzialanie = f"{liczba_1} + {liczba_2} = {wynik}"
        print("Wynik: ", dzialanie)

        liczba_1=0
        liczba_2=0


    elif menu_opcja == 2:

        try:
            liczba_1 = float(input("Pierwsza liczba: "))
            liczba_2 = float(input("Druga liczba: "))

        except ValueError:
            print("Blad: podaj prawidlowa liczbe.")
            continue


        wynik = liczba_1 - liczba_2
        dzialanie = f"{liczba_1} - {liczba_2} = {wynik}"
        print("Wynik: ", dzialanie)


        liczba_1 = 0
        liczba_2 = 0

    elif menu_opcja == 3:

        try:
            liczba_1 = float(input("Pierwsza liczba: "))
            liczba_2 = float(input("Druga liczba: "))

        except ValueError:
            print("Blad: podaj prawidlowa liczbe.")
            continue


        wynik = liczba_1 * liczba_2
        dzialanie = f"{liczba_1} * {liczba_2} = {wynik}"
        print("Wynik: ", dzialanie)


    if menu_opcja == 4:

        try:
            liczba_1 = float(input("Pierwsza liczba: "))
            liczba_2 = float(input("Druga liczba: "))

        except ValueError:
            print("Blad: podaj prawidlowa liczbe.")
            continue


        if liczba_2 == 0:
            print("Blad: nie mozna dzielic liczb przez zero.")
            continue


        wynik = liczba_1 / liczba_2


        dzialanie = f"{liczba_1} / {liczba_2} = {wynik}"
        print("Wynik: ", dzialanie)


    elif menu_opcja == 5:

        try:
            liczba_1 = float(input("Pierwsza liczba: "))
            liczba_2 = float(input("Druga liczba: "))

        except ValueError:
            print("Blad: podaj prawidlowa liczbe.")
            continue

        wynik = liczba_1 ** liczba_2

        dzialanie = f"{liczba_1} ** {liczba_2} = {wynik}"
        print("Wynik: ", dzialanie)


    elif menu_opcja == 6:

        try:
            ile_liczb = int(input("Ile liczb? "))

        except ValueError:
            print("Blad: podaj liczbe calkowita.")
            continue

        if ile_liczb <= 0:
            print("Blad: liczba elementow musi byc dodatnia.")
            continue

        suma=0

        for x in range (ile_liczb):
            liczba=input(f"Liczba {x+1}: ")

            suma = suma + liczba

        srednia = suma/ile_liczb
        dzialanie = f"Srednia z {ile_liczb} liczb = {srednia}"
        print(dzialanie)

    elif menu_opcja == 7:
        if len(rejestr) == 0:
            print("Rrejestr dzialan jest pusty.")
        else:
            print()
            print("Rejestr dzialan:")

            len_rejestr=len(rejestr)
            for i in range(len_rejestr):
                print(f"{ i + 1 }. { rejestr[i] }")


    elif menu_opcja!=0 or 1<= menu_opcja <=7:
        print("Blad: nieprawidlowa opcja menu.")

    elif menu_opcja==0:
        print("Koniec programu.")
        break


