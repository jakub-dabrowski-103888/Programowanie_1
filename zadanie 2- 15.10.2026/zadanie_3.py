
lista_produktow=[
    {"napoje": "Woda", "cena":3},
    {"napoje": "Sok", "cena":5},
    {"napoje": "Cola", "cena":6}
]

menu_value=0
suma=0

print("Menu")
print()
for x in  range(1,4):

    print(f"{x}. {lista_produktow[x]['napoje']} - {lista_produktow[x]['cena']}")

print("0.Zakoncz. ")


while True:
    try:
        menu_value = int(input("Wybierz opcje: "))

    except ValueError:
        print("Blad: podaj liczbe calkowita.")
        continue

    if menu_value==0:
        print("Lacznie do zaplaty: "+suma +" zl")
        break

    if menu_value not in (1, 2, 3):
        print("Blad: podales niewlasciwa opcje.")
        continue



    if menu_value==1 or menu_value==2 or  menu_value==3 :
        produkt = lista_produktow[menu_value - 1]
        suma += produkt["cena"]

        print(f"Wybrano: {produkt['napoje']}, cena: {produkt['cena']} zl  ")
