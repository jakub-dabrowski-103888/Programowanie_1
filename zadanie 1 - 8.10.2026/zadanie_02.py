#Zadanie 2. Koszyk zakupowy
import os
ocena=0

def uruchom():
    print("Zadanie-2")
    print()



    while True:
        try:

            liczba_punktow=int(input("Podaj liczbe punktow:"))
            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Musisz podać liczbę całkowitą punktow . Sprobuj ponownie.\n")

    if (0<=liczba_punktow<=49):
        ocena=2
    elif(50<=liczba_punktow<=59):
        ocena=3
    elif(60<=liczba_punktow<=69):
        ocena=3.5
    elif(70<=liczba_punktow<=79):
        ocena=4
    elif(80<=liczba_punktow<=89):
        ocena=4.5
    elif(90<=liczba_punktow<=100):
        ocena=5

    print("Liczba punktow:",liczba_punktow)
    print("Uzyskana ocena:",ocena)

    print("\n")

    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")