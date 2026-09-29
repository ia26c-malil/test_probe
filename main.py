hoehe = int(input("Höhe: "))

zeile = 1

while zeile <= hoehe:
    anzahl_zeichen = 0

    while anzahl_zeichen < hoehe - zeile:
        print(".", end="")
        anzahl_zeichen += 1

    zeile += 1