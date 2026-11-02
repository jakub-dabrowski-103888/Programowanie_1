print("Zadanie 3")

Pomiary=[]


alarm=50

liczba_produktow=int(input("Podaj liczbe pomiarow: "))
for x in range(liczba_produktow):
    value=int(input(f"pomiar {x+1} :"))
    Pomiary.append(value)

lista_alarm = [x for x in Pomiary if alarm <= x]
lista_podwojona=[x * 2 for x in Pomiary]



alarm_bool= any(x >= alarm for x in Pomiary)

sprawdzenie_pomiarow = all(x < alarm for x in Pomiary)





print(f"Pomiary alarmowe: {lista_alarm}")

print(f"Pomiary pomnozone przez 2: {lista_podwojona}")

value_alarm=""
if alarm_bool==True:
    value_alarm="Tak"
else:
    value_alarm="Nie"
print(f"Czy wystapil alarm?: {value_alarm}")

sprawdzenie_pomiarow_value=""
if sprawdzenie_pomiarow==True:
    sprawdzenie_pomiarow_value="Tak"
else:
    sprawdzenie_pomiarow_value="Nie"
print(f"Czy wszystkie pomiary sa prawidlowe?: {sprawdzenie_pomiarow_value}")

