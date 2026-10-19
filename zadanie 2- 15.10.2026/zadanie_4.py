
temperatury=[]
temp_srednia=0
min_temp=0
max_temp=0
powyzej_sredniej=[]
liczba_dni=0

for i in range(1,8):
    while True:
        try:
            temp_value = int(input(f"Dzien {i}: "))
            temperatury.append(temp_value)
            break
        except ValueError:
            print("Blad: podaj temperature jako liczbe calkowita.")

ilosc=len(temperatury)

temp_srednia=sum(temperatury)/ilosc

min_temp=min(temperatury)
max_temp=max(temperatury)

for i in range(ilosc):
    if temperatury[i] > temp_srednia:
        powyzej_sredniej.append(temperatury[i])


liczba_dni=len(powyzej_sredniej)

print(f"Srednia: {temp_srednia} C")
print(f"Najwyzsza: {max_temp} C")
print(f"Najnizsza: {min_temp} C")
print(f"Powyzej sredniej: {powyzej_sredniej}")
print(f"Liczba dni: {liczba_dni}")


