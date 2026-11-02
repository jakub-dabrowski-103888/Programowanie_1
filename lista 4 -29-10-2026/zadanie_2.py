print("zadanie 2")

Produkty=[]
ceny=[]

liczba_produktow=int(input("Podaj liczbe produktow: "))
for x in range(liczba_produktow):
    value=input(f"Produkt {x+1} :")
    Produkty.append(value)
    value_cena=input("Cena: ")
    ceny.append(value_cena)


print("========= Cennik ===========")
for numer, (produkt, cena) in enumerate(zip(Produkty, ceny), start=1):
    print(f"{numer}. {produkt} - {cena} zl")



suma=00.00

for cena in ceny:
    suma=suma+ float(cena)


print(f"Suma cen: {suma}")

najwieksza_cena= max(ceny)

for produkt, cena in zip(Produkty, ceny):
    if cena == najwieksza_cena:
        print(f"Najdroższy produkt: {produkt}, {cena} zl")


