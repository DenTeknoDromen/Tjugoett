import random
import time

color = ["Hjärter","Ruter","Klöver","Spader"]
kortnamn =["Två","Tre","Fyra","Fem","Sex","Sju",
           "Åtta","Nio","Tio","Knekt","Dam","Kung","Ess"]
pile = []
yourpile = []
cpupile = []
score = 0
cpuscore = 0

def drakort(humancheck, currpile, currscore):
    more = "y"
    while more == "y":
        value = random.randint(2,14)       
        kort = f"{color[random.randint(0,3)]} {kortnamn[value-2]}"
        if kort in pile:
            continue
        pile.append(kort)
        currpile.append(kort)
        print(f"{kort} \n")
        if value == 14:
            if humancheck:
                value = int(input("Du fick ett Ess! Välj värde genom att skriva 1 eller 14: "))
            elif humancheck == 0:
                value = 1     
        currscore += value
        if currscore > 21:
            break
        if humancheck:
            more = input("Vill du dra ett till kort? y/n: ").casefold()              
        elif currscore >= 14:
                more = "n"
        time.sleep(1)
    return currscore

print("--------------------")
print("Din tur: \n")
score = drakort(bool(1),yourpile, score)
print("--------------------")
if score > 21:
    print("Du förlorade!")
print(f"Här är din poäng: {score}")
print(f"Här är dina kort: {yourpile}")
time.sleep(2)
print("--------------------")
print("Datorns tur: \n")
cpuscore = drakort(bool(0),cpupile, cpuscore)
print("--------------------")
print(f"Här är datorns poäng: {cpuscore}")
print(f"Här är datorns kort: {cpupile}")
print("--------------------")
time.sleep(2)
if score <= 21 and score > cpuscore:
    print("Du vann! Grattis!")
else:
    print("Datorn vann")






