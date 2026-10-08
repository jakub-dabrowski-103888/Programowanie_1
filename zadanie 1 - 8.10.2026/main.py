

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

if(rabat_zad_3<=20):
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




