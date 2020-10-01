# Bestand in read-only (r) mode openen (wel zo veilig, we gaan niets overschrijven)
bestand = open("klasgenoten.txt", "r")

# Een tekst naar het bestand schrijven
#regel1 = bestand.readline()
#print(regel1)
#regel2 = bestand.readline()
#print(regel2)
#regel3 = bestand.readline()
#print(regel3)
#regel4 = bestand.readline()
#print(regel4)
#regel5 = bestand.readline()
#print(regel5)
#regel6 = bestand.readline()
#print(regel6)
#regel7 = bestand.readline()
#print(regel7)
#regel8 = bestand.readline()
#print(regel8)
#regel9 = bestand.readline()
#print(regel9)
#regel10 = bestand.readline()
#print(regel10)


# Eerste regel inlezen en opslaan in de variabele: tekst_regel
tekst_regel = bestand.readline()

# while loop gaat door zolang er iets in de variabele tekst_regel staat
while tekst_regel:
    # Let op: laat de code in de while loop 4 spaties inspringen!

    # De newline er af halen
    tekst_regel = tekst_regel.strip()

    # De regel op het scherm zetten:
    print(tekst_regel)

    # Volgende regel ophalen, zodat de while loop doorgaat
    tekst_regel = bestand.readline()



