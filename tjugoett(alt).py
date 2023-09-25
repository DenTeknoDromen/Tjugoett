import random
import time
import os

#                           ------Alternativ lösning som inte använder klasser-----
#                                       ------se tjugoettan.py-----

color = {1: "Hjärter", 2: "Ruter", 3: "Klöver", 4: "Spader"}
kortnamn = {2: "Två", 3: "Tre", 4: "Fyra", 5: "Fem", 6: "Sex", 7: "Sju",
            8: "Åtta", 9: "Nio", 10: "Tio", 11: "Knekt", 12: "Dam",
            13: "Kung", 14: "Ess"}
pile = []
yourpile = []
cpupile = []
score = 0
cpuscore = 0


# Används för att kolla om användar input är valid
# Funkar till alla input i programmet
def parse(opt1, opt2, inpt):
    if inpt == opt1 or inpt == opt2:
        return inpt
    else:
        return parse(opt1, opt2, input(f"Skriv antingen "
                                       f"{opt1} eller {opt2}: "))


# Huvudfunktion som används för att hålla spelet igång
# Används två gånger, en gång för användaren och en gång för datorn
def drakort(humancheck, currpile, currscore):
    more = "y"
    while more == "y":
        value = random.randint(2, 14)
        # Skapar ett kort som str genom att slumpa fram färg och valör
        kort = f"{color[random.randint(1,4)]} {kortnamn[value]}"
        # Kollar att kortet inte dragits redan
        if kort in pile:
            continue
        pile.append(kort)  # Pile innehåller gamla kort
        currpile.append(kort)
        print(f"{kort} \n")
        # Kollar genom parsefunktionen vilket värde användaren vill ha
        if value == 14:
            if humancheck:
                value = int(parse("1", "14", (input("Du fick ett Ess! Välj "
                                                    "värde genom att skriva 1 "
                                                    "eller 14: "))))
            elif humancheck == 0:  # Datorn väljer alltid 0
                value = 1
        currscore += value
        if currscore > 21:
            break
        if humancheck:
            more = parse("y", "n", input("Vill du dra ett till "
                                         "kort? y/n: ").casefold())
        # Datorn slutar alltid dra nya kort över 14 poäng
        elif currscore >= 14:
            more = "n"
        time.sleep(1)
    return currscore  # returnerar currscore till


if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

# Interface
print("--------------------")
print("Din tur:")
score = drakort(bool(1), yourpile, score)
print("--------------------")
if score > 21:
    print("Du förlorade!")
print(f"Här är din poäng: {score}")
print(f"Här är dina kort: {yourpile}")
time.sleep(2)
print("--------------------")
print("Datorns tur: \n")
cpuscore = drakort(bool(0), cpupile, cpuscore)
print("--------------------")
print(f"Här är datorns poäng: {cpuscore}")
print(f"Här är datorns kort: {cpupile}")
print("--------------------")
time.sleep(2)
if score <= 21 and score > cpuscore:
    print("Du vann! Grattis!")
else:
    print("Datorn vann")
