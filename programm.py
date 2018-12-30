import random

random.seed()

a = random.randint(1, 100)
b = random.randint(1, 100)

# Berechnung
c = a+b
Erg1 = 0

Versuch = 0
while Erg1 != c:
    # Ausgabe
    Versuch = Versuch + 1
    print("Versuch: Nr. ", Versuch, "\nDie Aufgabe:", a, "+", b)

    # Eingabe der Ergebnisses:
    print("Bitte geben Sie das Ergebnis ein:")
    Erg = input()

    # Umwandlung Ergrebnis in ganze Zahl
    try:
        Erg1 = int(Erg)
    except:
        print("Bitte geben Sie eine ganze Zahl ein! \n\nNeuer Versuch:")
        continue

    # Ausgabe des Ergebnisses
    if c == Erg1:
        print("Das Ergebnis ist richtig. Anzahl Versuche: ", Versuch)
    else:
        print("Das Ergebnis war falsch. \n\nNeuer Versuch:")
