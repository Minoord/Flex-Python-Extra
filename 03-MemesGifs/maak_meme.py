from PIL import Image,ImageFont, ImageDraw 
afbeelding = Image.open("dog-fire.jpg")
breedte = afbeelding.width
hoogte = afbeelding.height
print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")
print(afbeelding.format, afbeelding.size, afbeelding.mode)
lettertype = ImageFont.truetype("impact.ttf", 60)


# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(afbeelding) 
# Tekst schrijven
tekst = "it's just a Syntrax error"
# Bereken de breedte en hoogte van de tekst
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))
# Tekst positie berekenen
tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 1
# Denieuw berekende tekst_x en tekst_y gebruiken
tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))
tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))
# Het resultaat tonen
afbeelding.show()

# En opslaan onder een andere naam
afbeelding.save("meme_met_tekst.jpg")
