from PIL import Image
afbeelding = Image.open("Haikyuu-Episode-02-04.png")

# De afbeelding tonen in de standaard image viewer van jouw systeem
afbeelding.show()

# De breedte en hoogte van de afbeelding lezen en tonen 
breedte = afbeelding.width
hoogte = afbeelding.height

# Afmetingen op het scherm zetten
# Met str() zet je een int (getal) naar een string om. Dan kan print() het gebruiken.
print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

# Andere info uitlezen en tonen
print(afbeelding.format, afbeelding.size, afbeelding.mode)

