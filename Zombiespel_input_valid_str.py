# Zombie Spel


from random import randint

# Klassen som hanterar dörrarna, antal dörrar från start är samma som antal frågor
class Door:
    def __init__(self, no_doors):
        self.no_doors = no_doors
        self.doors = [0] * no_doors  # Skapar en lista
        self.zombie_door = randint(1, no_doors)  # Väljer en dörr för zombie

# class Zombie:
    # def __init__(self, door_number):
        # self.door_number = randint(1, no_questions - 1)

class Question:
    def __init__(self, table, operator):
        self.table = table
        self.operator = operator
        # self.random_number = randint(0, 12)  # Väljer en siffra mellan 0 och 12
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

# Huvudprogrammet, inlindat i en play_again loop för att hantera om spelaren vill spela igen
play_again = True
while play_again:

    # Frågar om antal frågor, tabell och räknesätt och kontrollerar att inmatningen är giltig
    fråga = input(f'Hur många frågor vill du ha? (12-39 st) ')
    svar = input_valid_int(fråga, "Ange giltigt svar!", 12, 39)

    fråga = input(f'Vilken tabell vill du öva på? (2-12) ')
    svar = input_valid_int(fråga, "Ange giltigt svar!", 2, 12)

    fråga = input(f'Vilken faktor vill du öva på? ( *, // eller %) ')
    svar = input_valid_str(fråga, "Ange giltigt svar!", ['*', '//', '%'])

    no_doors = Door(no_questions)
    current_question = 1
    keep_playing = True

    while keep_playing:
        zombie_door = no_doors.zombie_door
        random_number = randint(0, 12)

        # Ställer frågan och kontrollerar att svaret är ett heltal
        print(f'Fråga {current_question} av {no_questions}: Vad blir {random_number}{operator}{table}?') 
        valid_answer = False
        while not valid_answer:
            answer = input('Ditt svar: ')
            if answer.isdigit():
                valid_answer = True
            else:
                print('Felaktig inmatning, ange ett heltal.')
        correct_answer = str(eval(f'{random_number}{operator}{table}'))

        # Frågar om vilken dörr och kontrollerar att det är ett heltal och inom rätt intervall
        print(f'Vilken dörr vill du välja? (1-{no_doors.no_doors}) ')
        valid_door = False
        while not valid_door:
            try:
                chosen_door = int(input('Ditt val: '))
                if 1 <= chosen_door <= no_doors.no_doors:
                    valid_door = True
                else:
                    print(f'Felaktig inmatning, välj en dörr mellan 1 och {no_doors.no_doors}')
            except ValueError:
                print(f'Felaktig inmatning, ange ett heltal.')

        # Kontrollerar om spelaren svarade rätt och huruvia det fanns en zombie bakom den valda dörren
        if answer == correct_answer and chosen_door != zombie_door:
            print(f'Rätt svar!') 
            print(f'Zombien var bakom dörr: {zombie_door}')
            
            # Uppdaterar spelet för nästa fråga
            current_question += 1
            no_doors.no_doors -= 1
            if no_doors.no_doors > 1:
                no_doors.zombie_door = randint(1, no_doors.no_doors)
            
            # Spelaren har besvarata alla frågor och klarat spelet
            if current_question > no_questions:
                print(f'Grattis, du klarade spelet!')
                print(f'Zombien var bakom dörr: {zombie_door}')
                keep_playing = False

        # Om spelaren svarade rätt men valde en dörr med en zombie
        elif answer == correct_answer and chosen_door == zombie_door:
            print(f'Rätt svar men Zombien åt upp dig!')
            keep_playing = False

        # Om spelaren svarade rätt och har klarat alla frågor
        elif answer == correct_answer and current_question == no_questions and chosen_door != zombie_door:
            print('Grattis, du klarade spelet!')
            print(f'Zombien var bakom dörr: {zombie_door}')
            keep_playing = False

        # Om spelaren svarade fel
        else:
            print(f'Fel svar!')
            print(f'Zombien var bakom dörr: {zombie_door}')
            keep_playing = False

    # Frågar om spelaren vill spela igen och kontrollerat angivet svar är giltigt
    fråga = "Vill du spela igen (j/n)? "
    svar = input_valid_str(fråga, "Ange giltigt svar!", ('j', 'n'))
    if svar == 'n':
        print(f'Tack för att du spelade!')
        play_again = False
    elif svar == 'j':
        print(f'Startar om spelet...')
        play_again = True

