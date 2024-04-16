# Aufgabe 1-2 - Drucken
print("Willkommen", "bei", "Logiscool", sep=", ", end="\n_____________\n")
print("Du bist hier willkommen.", end="\n")

a = 42
b = "Apfel"
c = True
print(a, b, c)
print(str(a) + " " + b + " " + str(c))

# Aufgabe 3 - Typen
print(type(a))
print(type(b))
print(type(c))

# Aufgabe 4 - Ganzzahlen
print(123)          # Dezimalzahl
print(0o123)        # Oktalzahl
print(0x123)        # Hexadezimalzahl
print(bin(123))     # Binärzahl
print(0b101101)     # Binärzahl

# Aufgabe 5 - Gleitkommazahlen
a = 0.0002
b = 2e-4
print(a)
print(b)
print(0.0000000000000000000000001)

# Aufgabe 6 - Besondere Zeichen drucken
print("""'Das Lernen bei Logiscool war die beste Entscheidung meines Lebens!' - sagte der weise alte Mann
'Und was war deine schlechteste Entscheidung?' - fragte der Student
'Ich hätte früher anfangen können.'""")

# Aufgabe 7 - Operatoren
try:
    a = int(input("Erste Zahl:\n"))
    b = int(input("Zweite Zahl:\n"))
    if a > b:
        print("a=", a, " ist größer als b=", b, ".", sep="")
    elif a < b:
        print("b=", b, " ist größer als a=", a, ".", sep="")
    else:
        print("a=", a, " und b=", b, " sind gleich.", sep="")
except:
    print("Das kann ich nicht machen.")

# Aufgabe 8 - Prioritäten
print(5 * 25 % 8 + 100 / 2 * 8 // 2)
print(5 * 25 % (8 + 100 / 2 * 8 // 2))
print(5 * ((25 % 8) + 100) / 2 * 8 // 2)

# Aufgabe 9 - Klammern
print(3 + 20 % 4 ** 2 * 5 / 5 - 5)
print((3 + (((20 % (4 ** 2)) * 5) / 5)) - 5)

# Aufgabe 10 - Zufälliger Divisionsfehler
import random
try:
    for i in range(1, 10):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        e = random.randint(-10, 10)
        print(a/b/c/d/e)
except ZeroDivisionError:
    print("Mindestens eine Variable war Null.")
