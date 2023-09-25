import random
import os
import time

deck = []
playerscore = 0
cpuscore = 0
playertopscore = 0
cputopscore = 0
ui_width = 50

colors = ["Hjärter", "Ruter", "Klöver", "Spader"]
pointvalues = {"Två": 2, "Tre": 3, "Fyra": 4, "Fem": 5, "Sex": 6,
               "Sju": 7, "Åtta": 8, "Nio": 9, "Tio": 10, "Knekt": 11,
               "Dam": 12, "Kung": 13, "Ess": 1}


# använder värdena i listona "colors" och "pointvalues" för att skapa ett kort
class card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.pointvalue = pointvalues[self.value]

    # Låter spelaren välja värde på ess ifall det dras, default är alltid 1
    def choosevalue(self):
        msg = "Du drog ett Ess! Välj värde genom att skriva 1 eller 14: "
        while True:
            indata = input(msg)
            if indata == "1" or indata == "14":
                break
            else:
                msg = "Skriv antingen 1 eller 14: "
        return int(indata)

    def __str__(self):
        return f"{self.color} {self.value}"


# Tömmer listan deck och fyller den med 52 nya kort
def shuffle():
    deck.clear()
    for color in colors:
        for keys in pointvalues:
            deck.append(card(color, keys))


# Metod som körs varje gång spelaren drar ett kort
# Hanterar ifall ess dras och beräknar poäng
def playerdraw():
    time.sleep(1)
    i = random.randint(0, len(deck)-1)
    newcard = deck[i]
    print(f"\nNytt kort: {newcard}")
    # Kallar på choosevalue i card klassen ifall det nya kortet är ett ess
    if newcard.value == "Ess":
        newcard.pointvalue = newcard.choosevalue()
    global playerscore
    playerscore += newcard.pointvalue
    del deck[i]
    print(f"Poäng: {playerscore}")


# Metod som körs varje gång datorn drar ett kort
# Samma som playerdraw fast utan användar input
def cpudraw():
    time.sleep(1)
    i = random.randint(0, len(deck))
    newcard = deck[i]
    global cpuscore
    cpuscore += newcard.pointvalue
    del deck[i]
    print(f"\nDatorn drog: {newcard}")
    print(f"Poäng: {cpuscore}")


# Avgör vem som vinner och visar resulatet
def wincheck():
    global playerscore
    global playertopscore
    global cpuscore
    global cputopscore
    time.sleep(1)
    print("-" * ui_width)
    if playerscore > 21:
        cputopscore += 1
        print("Du fick över 21 poäng. Du förlorade.")
        cpuscore = "n/a"
    elif playerscore > cpuscore or cpuscore > 21:
        playertopscore += 1
        print("Du vann! Grattis!")
    else:
        cputopscore += 1
        print("Du förlorade.")

    print(f"Din poäng: {playerscore}")
    print(f"Datorns poäng: {cpuscore}")
    print("-" * ui_width)
    print(f"Du: {playertopscore}")
    print(f"Datorn: {cputopscore}")


# Hanterar och validerar spelar input
def parse(msg):
    msg = msg
    while True:
        indata = input(msg)
        if indata == "j" or indata == "n":
            break
        else:
            msg = "Skriv antingen j eller n: "
    return indata


# Nollställer poäng och kort, start ui och hanterar spel metoder
# Kallas rekursivt för att kunna spela flera rundor
def newgame():
    # Nollställer poäng och kort
    global playerscore
    playerscore = 0
    global cpuscore
    cpuscore = 0
    shuffle()
    # Rensar terminalen
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    # UI
    print(ui_width * "-")
    print("TJUGOETTAN".center(ui_width))
    print(ui_width * "-")
    print("Din tur")
    # Spelarens tur
    yncheck = "j"
    while yncheck == "j":
        playerdraw()
        if playerscore > 21:
            cpuscore = 999
            break
        yncheck = parse("Vill du dra ett nytt kort? skriv j/n: ")
    print("-" * ui_width)
    # Datorns tur
    if cpuscore != 999:
        print("Datorns tur")
        while cpuscore <= 14:
            cpudraw()
    # Kollar vem som vann och kollar om spelaren vill spela en ny runda
    wincheck()
    yncheck = parse("Vill du spela igen?: ")
    if yncheck == "j":
        newgame()
    else:
        print(ui_width * "-")


newgame()
