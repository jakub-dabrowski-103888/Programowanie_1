
#zadanie_6


import os

def uruchom():
    print("Zadanie-2")
    print()


    temperatura=0
    ogrzewanie=True
    powod=""

    while True:
        try:
            temperatura = int(input("Podaj temperature: "))

            break

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Musisz podać liczbę całkowitą . Spróbuj ponownie.\n")

    #####################

    while True:

        dom_osoby = input("Czy ktos jest w domu ? (tak/nie) : ").strip().lower()

        if dom_osoby == "tak" or dom_osoby == "nie":
            break


        print("Błąd: Musisz wpisać tak/nie. Spróbuj ponownie.\n")

    ######################

    while True:
        open_window = input("Czy okno jest otwarte (tak/nie)? : ").strip().lower()

        if dom_osoby == "tak" or dom_osoby == "nie":
            break

        print("Błąd: Musisz wpisać tak/nie. Spróbuj ponownie.\n")

    if(open_window=="tak"):
        ogrzewanie=False
        powod=""
    else:
        if(dom_osoby=="tak"):
            if(temperatura<20):
                ogrzewanie=True
                powod="Temperatura ponizej 20 C"
            else:
                ogrzewanie=False
                powod=""
        if(dom_osoby=="nie"):
            if (temperatura < 16):
                ogrzewanie = True
                powod = "Temperatura ponizej 16 C"
            else:
                ogrzewanie = False
                powod=""

    #interfejs
    print("\n")

    if(ogrzewanie==True):
        print("Ogrzewanie: WLACZONE\n")
        print("Powod: "+powod)
    elif(ogrzewanie==False):
        print("Ogrzewanie: WYLACZONE\n")
        print("Powod: "+powod)

    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")