hoehe = int(input("Höhe: "))

zeile = 1

while zeile <= hoehe:
    anzahl_zeichen = 0

    while anzahl_zeichen < hoehe - zeile:
        print(".", end="")
        anzahl_zeichen += 1

    zaehler = 0

    while zaehler < 2 * zeile - 1:
        print("*", end="")
        zaehler += 1

    print()
    zeile += 1

abstand = 0

while abstand < hoehe - 1:
    print(".", end="")
    abstand += 1

print("|")