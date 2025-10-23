import random as rand

namn = input("Vad heter du? ")
input(f"Hej {namn} och välkommen till spelet!")
slumptal = rand.randint(1, 10)
tal = input("Gissa ett tal mellan 1 och 10: ")
if tal == slumptal:
    print("Du gissade rätt!")
else:
    print(f"Tyvärr, det korrekta svaret var {slumptal}")