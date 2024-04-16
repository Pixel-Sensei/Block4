# Aufgabe 8 - Prioritäten

# Ausgabe des Ergebnisses der arithmetischen Operationen unter Berücksichtigung der Operatorprioritäten.
# 5 * 25 wird zuerst berechnet, dann wird 25 modulo 8 berechnet, das Ergebnis mit 5 multipliziert und der Rest wird verwendet.
# Dann wird 100 durch 2 geteilt und mit 8 multipliziert, das Ergebnis wird durch 2 geteilt und der Ganzzahlanteil wird verwendet.
# Schließlich werden die Ergebnisse der beiden vorherigen Operationen addiert.
print(5 * 25 % 8 + 100 / 2 * 8 // 2)

# Ausgabe des Ergebnisses der arithmetischen Operationen mit Klammern, um die Prioritäten zu ändern.
# Die Ausdrücke innerhalb der Klammern werden zuerst ausgewertet.
# In diesem Fall wird zuerst 100 durch 2 geteilt und mit 8 multipliziert, das Ergebnis wird durch 2 geteilt und der Ganzzahlanteil wird verwendet.
# Dann wird das Ergebnis mit 8 addiert und die Modulo-Operation mit 25 wird ausgeführt und mit 5 multipliziert.
print(5 * 25 % (8 + 100 / 2 * 8 // 2))

# Ausgabe des Ergebnisses der arithmetischen Operationen mit Klammern, um die Prioritäten zu ändern.
# Die Ausdrücke innerhalb der Klammern werden zuerst ausgewertet.
# In diesem Fall wird zuerst 25 modulo 8 berechnet, das Ergebnis wird mit 100 addiert, dann wird das Ergebnis durch 2 geteilt, mit 5 multipliziert,
# mit 8 multipliziert und das Ergebnis wird durch 2 geteilt und der Ganzzahlanteil wird verwendet.
print(5 * ((25 % 8) + 100) / 2 * 8 // 2)
