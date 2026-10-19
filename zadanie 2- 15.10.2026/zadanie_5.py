

haslo="Python123"

proby=3

haslo_input=""

while True:
    haslo_input=str(input("Podaj haslo: "))

    if haslo_input==haslo:
        print("Logowanie udane !")
        break


    if haslo_input!=haslo:
        proby-=1

        if proby>0:
            print(f"Niepoprawne haslo. Pozostale proby: {proby}")
        elif proby<=0:
            print("Niepoprawne haslo. Konto zablokowane.")
            break


