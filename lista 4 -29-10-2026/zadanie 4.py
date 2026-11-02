print("Zadanie 4")

warsztat_python = set()
warsztat_ai = set()

while True:
    print("\n--- REJESTR UCZESTNIKÓW ---")
    print("1. Zapisz na Python")
    print("2. Zapisz na AI")
    print("3. Wyświetl uczestników")
    print("4. Uczestnicy obu warsztatów")
    print("5. Wszyscy unikalni uczestnicy")
    print("0. Zakończ")

    wybor = int(input("Wybierz opcję: "))

    if wybor == 0:
        print("Koniec programu.")
        break

    elif wybor not in [1, 2, 3, 4, 5]:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")

    elif wybor == 1:
        imie = input("Podaj imię: ").strip()
        nazwisko = input("Podaj nazwisko: ").strip()

        uczestnik = (imie, nazwisko)

        imie_porownanie = imie.lower()
        nazwisko_porownanie = nazwisko.lower()

        bool_value=False

        for i in warsztat_python:
            if i[0].lower() == imie_porownanie and i[1].lower() == nazwisko_porownanie:
                bool_value = True

        if bool_value:
            print("Ten uczestnik jest już zapisany na zajecia warsztatowe.")
        else:
            warsztat_python.add(uczestnik)
            print("Dodano uczestnika.")

    elif wybor == 2:

        imie = input("Podaj imię: ").strip()
        nazwisko = input("Podaj nazwisko: ").strip()

        uczestnik = (imie, nazwisko)

        imie_porownanie = imie.lower()
        nazwisko_porownanie = nazwisko.lower()

        bool_value = False

        for i in warsztat_python:
            if i[0].lower() == imie_porownanie and i[1].lower() == nazwisko_porownanie:
                bool_value = True

        if bool_value:
            print("Ten uczestnik jest już zapisany na zajecia warsztatowe.")
        else:
            warsztat_ai.add(uczestnik)
            print("Dodano uczestnika.")

    elif wybor == 3:

        print("\nUczestnicy warsztatu Python:")

        for imie, nazwisko in warsztat_python:
            print(imie, nazwisko)

        print("\nUczestnicy warsztatu AI:")

        for imie, nazwisko in warsztat_ai:
            print(imie, nazwisko)

    elif wybor == 4:
        wspolni = warsztat_python & warsztat_ai

        print("\nUczestnicy obu warsztatów:")

        for imie, nazwisko in wspolni:
            print(imie, nazwisko)

    elif wybor == "5":
        wszyscy = warsztat_python | warsztat_ai

        print("\nWszyscy unikalni uczestnicy:")

        for imie, nazwisko in wszyscy:
            print(imie, nazwisko)