import os

def wyznacz_ocene(punkty):
    if 0 <= punkty <= 49:
        return 2.0
    elif punkty <= 59:
        return 3.0
    elif punkty <= 69:
        return 3.5
    elif punkty <= 79:
        return 4.0
    elif punkty <= 89:
        return 4.5
    else:
        return 5.0


print("Zadanie-2")
print()


studenci_z_zaliczeniem = 0
lista_studentow = []
srednia=0.0
liczba_studentow=0
najwyzszy_wynik=0
najnizszy_wynik=0
wyniki_rosnaco=[]
x=[]
suma_punktow=0

while True:
    try:
        liczba_studentow = int(input("Podaj liczbe studentow: "))
        if liczba_studentow > 0:
            break
        print("Liczba studentów musi być większa od zera\n")


    except ValueError:
        print("Błąd: Musisz podać liczbę całkowitą.\n")


print()

for i in range(1, liczba_studentow + 1):
    nazwisko = input(f"\nNazwisko studenta {i}: ").strip()

    while True:
        try:
            punkty = int(input("Punkty (0-100): "))

            if 0 <= punkty <= 100:
                suma_punktow += punkty
                x.append(punkty)
                break

            print("Nieprawidlowa liczba punktow. Sprobuj ponownie.")

        except ValueError:
            print("Blad: podaj liczbe calkowita.")

    ocena = wyznacz_ocene(punkty)
    lista_studentow.append((nazwisko, punkty, ocena))

    if ocena >= 3.0:
        studenci_z_zaliczeniem += 1


# srednia

srednia=suma_punktow/liczba_studentow
wyniki_rosnaco= sorted(x)
najwyzszy_wynik=max(x)
najnizszy_wynik=min(x)




print("\nWyniki studentów:")


for nazwisko, punkty, ocena in lista_studentow:
    print(f"{nazwisko} - {punkty} pkt - ocena {ocena:.1f}")

print(f"Srednia: {srednia}")
print(f"Najwyzszy wynik: {najwyzszy_wynik}")
print(f"Najnizszy wynik: {najnizszy_wynik}")
print(f"Wyniki rosnaco: {wyniki_rosnaco}")
print(f"Liczba studentow, ktorzy zaliczyli: {studenci_z_zaliczeniem}")


print(f"\nLiczba studentów, którzy zaliczyli: {studenci_z_zaliczeniem}")


input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")