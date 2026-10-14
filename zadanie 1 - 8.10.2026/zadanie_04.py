#zadanie_4
import os

def uruchom():
    print("Zadanie-4")
    print()
    zgoda_bool=True
    dokument_bool=True

    wiek=int(input("Podaj wiek: "))

    zgoda=str(input("Czy jest zgoda opiekuna ? :")).strip().lower()

    if(zgoda=="tak"):
        zgoda_bool=True
    elif(zgoda=="nie" ):
        zgoda_bool=False

    dokument=str(input("Czy masz dokument tozsamości ? :")).strip().lower()

    if(dokument=="tak" ):
        dokument_bool=True
    elif(dokument=="nie" ):
        dokument_bool=False

    print("\n")

    if(dokument_bool==True):
        if(wiek>=18):
            print("Wypożyczenie możliwe")
        elif(13<wiek<17):
            if(zgoda_bool==False):
                print("Wypożyczenie niemożliwe")
            elif (zgoda_bool == False):
                print("Wypożyczenie niemożliwe")
        elif(wiek<=13):
            print("Wypożyczenie niemożliwe")
    else:
        print("Wypożyczenie niemożliwe")

    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")