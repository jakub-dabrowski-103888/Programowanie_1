


zakupy=[]
licznik=0

while True:
    try:
        ilosc = int(input("Ile produktow chcesz dodac? : "))

        if ilosc >= 0:
            break
        elif ilosc<0:
            print("Liczba produktow nie moze byc ujemna.")
        elif ilosc==0:
            print("Liczba produktow nie moze byc rowna 0.")


    except ValueError:
        print("Blad: podaj liczbe calkowita.")

for x in range (1, ilosc+1):
    produkt=str(input(f"\nProdukt {x} :"))
    zakupy.append(produkt)

print(f"Lista: {zakupy}")
licznik=len(zakupy)

while True:
    to_delete=str(input("Produkt do usuniecia :"))

    if to_delete=="":
        print("blad: nie wprowadziles produktu")
    elif to_delete in zakupy:
        zakupy.remove(to_delete)
        break
    else:
        print("Podany produkt nie znajduje sie na liscie. Sproboj ponownie")

print(f"Nowa Lista: {zakupy}")

