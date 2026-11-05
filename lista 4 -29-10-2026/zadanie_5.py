import os

def get_dodawanie(a, b):
    return a + b

def get_odejmowanie(a, b):
    return a - b

def get_mnozenie(a, b):
    return a * b

def get_dzielenie(a, b):
    if b == 0:
        return None
    return a / b

def get_potegowanie(a, b):
    return a ** b

def get_srednia(liczby):

    if not liczby:
        return 0
    return sum(liczby) / len(liczby)

def Menu_views():
    print("\n========== Kalkulator  ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("7. Rejestr dzialan na kalkulatorze")
    print("0. Zakoncz")
    print("=======================================")

def main():
    print("Zadanie 2 \n")
    rejestr = []

    while True:
        Menu_views()

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

            wynik = get_dodawanie(liczba_1, liczba_2)
            dzialanie = f"{liczba_1} + {liczba_2} = {wynik}"
            print("Wynik: ", dzialanie)
            rejestr.append(dzialanie)

        elif menu_opcja == 2:
            try:
                liczba_1 = float(input("Pierwsza liczba: "))
                liczba_2 = float(input("Druga liczba: "))
            except ValueError:
                print("Blad: podaj prawidlowa liczbe.")
                continue

            wynik = get_odejmowanie(liczba_1, liczba_2)
            dzialanie = f"{liczba_1} - {liczba_2} = {wynik}"
            print("Wynik: ", dzialanie)
            rejestr.append(dzialanie)

        elif menu_opcja == 3:
            try:
                liczba_1 = float(input("Pierwsza liczba: "))
                liczba_2 = float(input("Druga liczba: "))
            except ValueError:
                print("Blad: podaj prawidlowa liczbe.")
                continue

            wynik = get_mnozenie(liczba_1, liczba_2)
            dzialanie = f"{liczba_1} * {liczba_2} = {wynik}"
            print("Wynik: ", dzialanie)
            rejestr.append(dzialanie)

        elif menu_opcja == 4:
            try:
                liczba_1 = float(input("Pierwsza liczba: "))
                liczba_2 = float(input("Druga liczba: "))
            except ValueError:
                print("Blad: podaj prawidlowa liczbe.")
                continue

            wynik = get_dzielenie(liczba_1, liczba_2)
            if wynik is None:
                print("Blad: nie mozna dzielic liczb przez zero.")
                continue

            dzialanie = f"{liczba_1} / {liczba_2} = {wynik}"
            print("Wynik: ", dzialanie)
            rejestr.append(dzialanie)

        elif menu_opcja == 5:
            try:
                liczba_1 = float(input("Pierwsza liczba: "))
                liczba_2 = float(input("Druga liczba: "))
            except ValueError:
                print("Blad: podaj prawidlowa liczbe.")
                continue

            wynik = get_potegowanie(liczba_1, liczba_2)
            dzialanie = f"{liczba_1} ** {liczba_2} = {wynik}"
            print("Wynik: ", dzialanie)
            rejestr.append(dzialanie)

        elif menu_opcja == 6:
            try:
                ile_liczb = int(input("Ile liczb? "))
            except ValueError:
                print("Blad: podaj liczbe calkowita.")
                continue

            if ile_liczb <= 0:
                print("Blad: liczba elementow musi byc dodatnia.")
                continue

            pobrane_liczby = []
            for x in range(ile_liczb):
                while True:
                    try:
                        liczba = float(input(f"Liczba {x+1}: "))
                        pobrane_liczby.append(liczba)
                        break
                    except ValueError:
                        print("Blad: podaj prawidlowa liczbe.")

            srednia = get_srednia(pobrane_liczby)
            dzialanie = f"Srednia z {ile_liczb} liczb = {srednia}"
            print("Wynik: ", dzialanie)
            rejestr.append(dzialanie)

        elif menu_opcja == 7:
            if len(rejestr) == 0:
                print("Rejestr dzialan jest pusty.")
            else:
                print("\nRejestr dzialan:")
                for i in range(len(rejestr)):
                    print(f"{i + 1}. {rejestr[i]}")

        elif menu_opcja == 0:
            print("Koniec programu.")
            break
        else:
            print("Blad: nieprawidlowa opcja menu.")

if __name__ == "__main__":
    main()