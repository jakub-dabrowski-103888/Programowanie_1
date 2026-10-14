
#Zadanie 1. Koszyk zakupowy
import os

koszt_dostawy=12.00
koszt_caly=0.00
def uruchom():
    print("Zadanie-1")
    print()



    while True:
        try:
            cena_produktu= float(input("Podaj cene produktu : "))
            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: podaj poprawna wartosc ceny. Spróbuj ponownie.\n")

    while True:
        try:
            liczba_sztuk= int(input("Podaj liczbe sztuk: "))
            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: podaj poprawna ilość sztuk. Spróbuj ponownie.\n")





    koszt_caly=cena_produktu*liczba_sztuk


    if(koszt_caly>100):
        koszt_dostawy=0
    else:
        koszt_dostawy=12

    koszt_ostateczny=koszt_caly+koszt_dostawy

    print("Wartosc produktow:",koszt_caly)
    print("Koszt dostawy:" ,koszt_dostawy)
    print("Do zaplaty:" , koszt_ostateczny)

    print("\n")

    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")