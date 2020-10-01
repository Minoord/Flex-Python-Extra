# importeert io
import io

#r = reading (lezen)
#w = writing (overschrijven)
#a = appending (toevoegen aan einde)
#t = text mode (voor tekstbestanden, dit is standaard)
#b = binary mode (binaire mode)


# Zo open je een bestand om naar te schrijven 
bestand = open("test.txt", "w")

# Een tekst naar het bestand schrijven
bestand.write("Test 123!");  

# Vergeet bestand niet te sluiten!
bestand.close()

#De code hier onder doet het niet
#omdat je zegt dat hij het bestand moet lezen
# en daarna geef je het de opdracht om er iets in te schrijven
# dan zegt de computer van ik kan niet schrijven, want ik moest lezen.
# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven")
