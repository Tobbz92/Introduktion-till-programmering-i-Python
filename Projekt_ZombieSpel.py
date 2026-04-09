# Zombie Spel


from random import random, randint, choice
import math

# Klassen som hanterar dörrarna, antal dörrar från start är samma som antal frågor
class Door:
    def __init__(self, no_doors):
        self.no_doors = no_doors
        self.doors = [0] * no_doors  # Skapar en lista
        self.zombie_door = randint(0, no_doors - 1)  # Väljer en dörr för zombie

class Zombie:
    def __init__(self, door_number):
        self.door_number = randint(0, no_questions - 1)

class Question:
    def __init__(self, table, operator):
        self.table = table
        self.operator = operator
        self.random_number = randint(0, 12)  # Väljer en siffra mellan 0 och 12
        self.current_question = current_question
        while self.current_question <= self.no_questions:
            self.current_question += 1
def input_valid_str(fråga, feltext, möjliga_svar):
    svar = input(fråga)
    while svar not in möjliga_svar:
        svar = input(f'{feltext}\n{fråga}')

    return svar

def input_valid_int(fråga, feltext, min, max):
    while True:  # Loopa tills korrekt värde skrivs in
        str = input(fråga)
        if str.isdigit() and min <= int(str) <= max:
            return int(str)  # Korrekt tal, returnera värdet
        print(feltext)
lenght = len('För att klara spelet behöver du svara rätt på alla frågor och undvika Zombisarna!)')
print('-' * lenght)
print('Välkommen till Zombie spelet!')
print('För att klara spelet behöver du svara rätt på alla frågor och undvika Zombisarna!)')
print('-' * lenght)


no_questions = int(input(f'Hur många frågor vill du ha? (12-39 st) '))
try:
    if 2 < no_questions < 40:
        pass
except ValueError:
    print('Felaktig inmatning')

no_doors = Door(no_questions)
table = int(input(f'Vilken tabell vill du öva på? (2-12) '))
try:
    if 1 < table < 13:
        pass
except ValueError:
    print('Felaktig inmatning')

operator = input(f'Vilken faktor vill du öva på? ( *, // eller %) ')
try:
    if operator in ['*', '//', '%']:
        pass
except ValueError:
    print('Felaktig inmatning')

keep_playing = True
while keep_playing:

    zombie_door = no_doors.zombie_door
    current_question = 1
    random_number = randint(0, 12)
    print(f'Fråga {current_question} av {no_questions}: Vad blir {random_number}{operator}{table}?') 
    answer = input('Ditt svar: ')
    print(f'Vilken dörr vill du välja? (1-{no_questions}) ')
    chosen_door = int(input('Ditt val: '))
    if answer == str(eval(f'{random_number}{operator}{table}')) and chosen_door != zombie_door:
        current_question += 1
        no_doors.no_doors -= 1
        print('Rätt svar!') 
        print(f'Zombien var bakom dörr: {zombie_door}')
        zombie_door = randint(0, no_doors.no_doors - 1)
    elif answer == str(eval(f'{random_number}{operator}{table}')) and chosen_door == zombie_door:
        print('Rätt svar men Zombien åt upp dig!')
    elif current_question == no_questions and chosen_door != zombie_door:
        print('Grattis, du klarade spelet!')
        print(f'Zombien var bakom dörr: {zombie_door}')
        fråga = "Vill du spela igen (j/n)? "
        svar = input_valid_str(fråga, "Ange giltigt svar!", ('j', 'n'))
        if svar == 'n':
            keep_playing = False
            print('Tack för att du spelade!')
        else:
            print('Okej, vi kör igen!')
    else:
        print('Fel svar!')
        print(f'Zombien var bakom dörr: {zombie_door}')
        fråga = "Vill du spela igen (j/n)? "
        svar = input_valid_str(fråga, "Ange giltigt svar!", ('j', 'n'))
        if svar == 'n':
            keep_playing = False
            print('Tack för att du spelade!')
        else:
            print('Okej, vi kör igen!')
