
#zadanie_5


import os


def uruchom():
    print("Zadanie-2")
    print()
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


    input("\nZadanie zakonczone. Nacisnij Enter, aby wrocic do menu...")
    os.system("cls" if os.name == "nt" else "clear")