import os

#Zadanie 1. Koszyk zakupowy

koszt_dostawy=12.00
koszt_caly=0.00

cena_produktu= float(input("Podaj cene produktu : "))

liczba_sztuk= float(input("Podaj liczbe sztuk: "))

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
#########################################################################

#Zadanie 2. Koszyk zakupowy

ocena=0

liczba_punktow=int(input("Podaj liczbe punktow:"))

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
###########################################################

#zadanie_3

cena_produktu_zad_3=float(input("Podaj cene produktu:"))
rabat_zad_3=int(input("Podaj rabat (%):"))

tekst=""

if(rabat_zad_3>=20):
    tekst="Duża Promocja"
else:
    tekst="Standardowa Promocja"

x=float(rabat_zad_3)/100
kwota_rabatu=cena_produktu_zad_3*x

cena_po_rabacie=kwota_rabatu+cena_produktu_zad_3


print("Cena poczatkowa:",cena_produktu_zad_3)
print("Kwota rabatu:",kwota_rabatu)
print("Cena po rabacie:",cena_produktu_zad_3)
print(tekst)

#######################################################################################################################

#zadanie_4

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


###########################################################

#zadanie_5
czas_parkowania=0
koszt=0

while True:
    czas_parkowania=int(input("Podaj czas parkowania (h): "))

    if(czas_parkowania>0):
        break

if(czas_parkowania==1):
    koszt=5
elif(1<czas_parkowania<=3):
    koszt=12
elif(3<czas_parkowania<=6):
    koszt=20
elif(czas_parkowania<6):
    koszt=30


print("Czas postoju: "+czas_parkowania+" godzin")
print("Oplata za parking: "+koszt+" zl")

###########################################################

#zadanie_6
temperatura=0
ogrzewanie=True
powod=""

while True:
    try:
        temperatura = int(input("Podaj temperature: "))

        break  # Przerywamy pętlę, bo mamy poprawną wartość

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


#######################################################################################################################
#Zadanie 7

oszczednosci=0
kwota_odkladana=0
ilosc_tygodni=0

while True:
    try:

        kwota_odkladana = int(input("ile odkladasz tygodniowo? : "))

        if kwota_odkladana < 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Kwota oszczędności nie może być ujemna. Sprobuj ponownie.\n")
            continue

        break

    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")

while True:
    try:

        kwota_odkladana = int(input("Przez ile tygodni? : "))

        if ilosc_tygodni <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: Liczba tygodni musi być wieksza niz zero. Sprobuj ponownie.\n")
            continue  # Wracamy

        break

    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")

print()

for tydzien in range(1, ilosc_tygodni + 1):
    oszczednosci += kwota_odkladana
    print(f"Tydzien {tydzien}: {oszczednosci} zl")

print()
print(f"Laczne oszczednosci: {oszczednosci} zl")



#######################################################################################################################
#Zadanie 8

wysokosc=0


while True:
    try:

        wysokosc = int(input("Podaj wysokosc choinki : "))

        if wysokosc <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd: wysokosc choinki musi byc wieksza niz zero. Sprobuj ponownie.\n")
            continue

        break

    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Błąd: Musisz podać liczbę całkowitą . Sprobuj ponownie.\n")

print()

for i in range(wysokosc):
    spacje = " " * (wysokosc - 1 - i)
    gwiazdki = "*" * (2 * i + 1)
    print(spacje + gwiazdki)

#######################################################################################################################
#Zadanie 9
