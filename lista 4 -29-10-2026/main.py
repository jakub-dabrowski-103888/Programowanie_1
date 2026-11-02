print("zadanie 1")

Pomiary=[]


def wyswietl_pomiary(pomiary):

     if len(pomiary) <= 6:
          print("Wszystkie dostępne pomiary:")
          for p in pomiary:
               print(p)
     else:
          print("Trzy pierwsze pomiary:")
          for p in pomiary[:3]:
               print(p)

          print("\nTrzy ostatnie pomiary:")
          for p in pomiary[-3:]:
               print(p)



#1
liczbaPomiarow=int(input("Podaj liczbe pomiarow:"))
for x in range (liczbaPomiarow):
     val=input(f" Pomiar {x+1} :")
     Pomiary.append(val)

print(f"Pierwszy pomiar : {Pomiary[0]}" )
rozmiar= len(Pomiary)
print(f"Ostani pomiar: {Pomiary[rozmiar-1]}" )

wyswietl_pomiary(Pomiary)

co_drugi_pomiar = Pomiary[::2]
odwrotna_kolejnosc= Pomiary[::-1]
kopia=Pomiary.copy()
kopia[0]=0

print(f"Co drugi pomiar: {co_drugi_pomiar}"  )
print(f"Odwrocona Lista: {odwrotna_kolejnosc}")
print(f"Oryginal: {Pomiary}")
print(f"Kopia po zmianie: {kopia}")


