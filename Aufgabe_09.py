# Aufgabe 9 - Klammern

# Berechnung mit Standardprioritäten:
# Zuerst wird 4 ** 2 (also 16) berechnet.
# Dann wird 20 modulo 16 (also 4) berechnet.
# Das Ergebnis wird mit 5 multipliziert, dann durch 5 geteilt, und schließlich von 5 subtrahiert.
print(3 + 20 % 4 ** 2 * 5 / 5 - 5)

# Berechnung mit geänderten Prioritäten durch Klammern:
# Hier werden Klammern verwendet, um die Reihenfolge der Operationen zu ändern.
# Zuerst wird 4 ** 2 (also 16) berechnet.
# Dann wird 20 modulo 16 (also 4) berechnet.
# Das Ergebnis wird mit 5 multipliziert, dann durch 5 geteilt, und schließlich von 5 subtrahiert.
# Die äußeren Klammern sorgen dafür, dass die Subtraktion von 5 am Ende durchgeführt wird.
print((3 + (((20 % (4 ** 2)) * 5) / 5)) - 5)
