from random import randint


# Hanterar felinmatning av frågor som text och kontrollerar möjliga svar
def input_valid_str(prompt, error_text, möjliga_svar):
    answer = input(prompt)
    while answer not in möjliga_svar:
        answer = input(f'{error_text}\n{prompt}')
    return answer

# Hanterar felinmatning av siffror och kontrollerar intervallet
def input_valid_int(prompt, error_text, min_value, max_value):
    while True:  # Loopa tills korrekt värde skrivs in
        answer = input(prompt)
        if answer.isdigit() and min_value <= int(answer) <= max_value:
            return int(answer)  # Korrekt tal, returnera värdet
        else:
            print(error_text)

# Klass för att hantera frågor
class Question:
    # Initierar klassen med tabell, operator och en lista för att hålla koll på ställda frågor
    def __init__(self, table, operator):
        self.table = table
        self.operator = operator
        self.number = randint(0, 12)  # Väljer en siffra mellan 0 och 12
        self.question = f'{self.number}{self.operator}{self.table}'  # Skapar
        self.asked_question = []
    
    # Sätter hur många gånger en fråga får upprepas baserat på antalet valda frågor
    def max_repeated_questions(self, no_questions):
        if 12 <= no_questions <= 13:
            return 1
        elif 14 <= no_questions <= 26:
            return 2
        elif 27 <= no_questions <= 39:
            return 3

    # Genererar en ny fråga och kontrollerar att den inte har ställts för många gånger
    def get_question(self, no_questions):
        max_times = self.max_repeated_questions(no_questions)

        while True:
            self.number = randint(0, 12)
            self.question = f"{self.number}{self.operator}{self.table}"

            if self.asked_question.count(self.question) < max_times:
                self.asked_question.append(self.question)
                return self.question
    
    # Hanterar svaret på frågan
    def get_correct_answer(self):
        if self.operator == '*':
            return self.number * self.table
        elif self.operator == '//':
            return self.number // self.table
        elif self.operator == '%':
            return self.number % self.table

    def __str__(self):
        return self.question

# Klass för att hantera dörrar och zombiens position   
class Door:
    def __init__(self, no_doors):
        self.no_doors = no_doors
        self.zombie_door = randint(1, no_doors)

# Huvudprogrammet, inlindat i en play_again loop för att hantera om spelaren vill spela igen
play_again = True
ask_new_settings = True
answer_scope = None
answer_table = None
answer_operator = None

while play_again:
    if ask_new_settings:
        answer_scope = input_valid_int('Hur många frågor vill du ha? (12-39 st) ', 'Ange giltigt svar!', 12, 39)
        answer_table = input_valid_int('Vilken tabell vill du öva på? (2-12) ', 'Ange giltigt svar!', 2, 12)
        answer_operator = input_valid_str('Vilken faktor vill du öva på? ( *, // eller %) ', 'Ange giltigt svar!', ['*', '//', '%'])

    keep_playing = True
    current_question = 1
    no_doors = Door(answer_scope)
    game_won = False
    question = Question(answer_table, answer_operator)

    # Loop som hanterar spelets gång, ställer frågor och hanterar dörrval
    while keep_playing and current_question <= answer_scope:
        question_text = question.get_question(answer_scope)
        valid_answer = False

        print(f'Fråga {current_question} av {answer_scope}: Vad blir {question}?')

        while not valid_answer:
            answer = input('Ditt svar: ')
            if answer.isdigit():
                valid_answer = True
            else:
                print('Felaktig inmatning, ange ett heltal.')

        correct_answer = question.get_correct_answer()

        # Kontrollerar svaret och hanterar dörrvalet
        if int(answer) == int(correct_answer):
            if current_question == answer_scope:
                print('Grattis, du klarade spelet!')
                keep_playing = False
                game_won = True
            else:
                zombie_door = no_doors.zombie_door
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
                        print('Felaktig inmatning, ange ett heltal.')

                # Kontrollerar om spelaren valde rätt dörr och uppdaterar spelet
                if chosen_door != zombie_door:
                    print('Rätt svar!')
                    print(f'Zombien var bakom dörr: {zombie_door}')
                    current_question += 1
                    no_doors.no_doors -= 1
                    if no_doors.no_doors >= 1:
                        no_doors.zombie_door = randint(1, no_doors.no_doors)
                else:
                    print('Rätt svar men Zombien åt upp dig!')
                    keep_playing = False
        else:
            print('Fel svar!')
            keep_playing = False

    # Frågar om spelaren vill spela igen och hanterar svaret
    answer_restart = input_valid_str('Vill du spela igen? (j/n) ', 'Ange giltigt svar!', ['j', 'n'])
    if answer_restart == 'n':
        print('Tack för att du spelade!')
        play_again = False
    else:
        ask_new_settings = game_won

    # Skriver ut de ställda frågorna för att kontrollera att de inte ställdes för många gånger.
    # question_list = question.asked_question
    # print('Ställda frågor:', question_list)

