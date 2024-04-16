# Aufgabe 7 - Operatoren

try:
    # Benutzereingabe für die erste Zahl
    a = int(input("Erste Zahl:\n"))
    # Benutzereingabe für die zweite Zahl
    b = int(input("Zweite Zahl:\n"))

    # Überprüfung, ob a grösser als b ist
    if a > b:
        print("a=", a, " ist grösser als b=", b, ".", sep="")
    # Überprüfung, ob b grösser als a ist
    elif a < b:
        print("b=", b, " ist grösser als a=", a, ".", sep="")
    # Wenn weder a noch b grösser sind, dann sind sie gleich
    else:
        print("a=", a, " und b=", b, " sind gleich.", sep="")

# Fehlerbehandlung, falls eine Ausnahme auftritt (z. B. wenn die Benutzereingabe keine ganze Zahl ist)
except:
    print("Das kann ich nicht machen.")  # Ausgabe einer Fehlermeldung
