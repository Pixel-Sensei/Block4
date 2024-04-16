# Aufgabe 10 - Zufälliger Divisionsfehler

# Importieren des Moduls random für die Verwendung von Zufallszahlen
import random

# Verwendung einer try-except-Struktur, um einen Divisionsfehler abzufangen
try:
    # Schleife, um 10 Zahlenpaare zu generieren und zu teilen
    for i in range(1, 10):
        # Generierung von 5 Zufallszahlen im Bereich von -10 bis 10
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        e = random.randint(-10, 10)
        # Division der Zahlen und Ausgabe des Ergebnisses
        print(a/b/c/d/e)
# Abfangen der ZeroDivisionError-Ausnahme, die auftritt, wenn mindestens eine Variable Null ist
except ZeroDivisionError:
    print("Mindestens eine Variable war Null.")
