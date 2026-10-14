import os

import zadanie_01
import zadanie_02
import zadanie_03
import zadanie_04
import zadanie_05
import zadanie_06
import zadanie_07
import zadanie_08
import zadanie_09
import zadanie_10


wybor=0

while True:
    print("================================")
    print("       LISTA I")
    print("================================")
    print()
    print("1. Zadanie 1")
    print("2. Zadanie 2")
    print("3. Zadanie 3")
    print("4. Zadanie 4")
    print("5. Zadanie 5")
    print("6. Zadanie 6")
    print("7. Zadanie 7")
    print("8. Zadanie 8")
    print("9. Zadanie 9")
    print("10. Zadanie 10")
    print("11. Wyjscie z programu")
    print()

    while True:
        try:
            wybor = int(input("Wybierz numer zadania: "))

            if 1 <= wybor <= 11:
                break
            else:
                print("Wybierz liczbe od 1 do 11.")

        except ValueError:
            print("Blad: Wpisz liczbe od 1 do 11.")

    if wybor == 1:
        zadanie_01.uruchom()
    elif wybor == 2:
        zadanie_02.uruchom()
    elif wybor == 3:
        zadanie_03.uruchom()
    elif wybor == 4:
        zadanie_04.uruchom()
    elif wybor == 5:
        zadanie_05.uruchom()
    elif wybor == 6:
        zadanie_06.uruchom()
    elif wybor == 7:
        zadanie_07.uruchom()
    elif wybor == 8:
        zadanie_08.uruchom()
    elif wybor == 9:
        zadanie_09.uruchom()
    elif wybor == 10:
        zadanie_10.uruchom()
    elif wybor == 11:
        print("Koniec programu.")
        break

    if wybor != 11:
        input("\nNacisnij Enter, aby wrocic do menu...")

    print("\n")

