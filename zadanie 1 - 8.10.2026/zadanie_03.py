#zadanie_3
import os


def uruchom():
    print("Zadanie-3")
    print()
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


    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")