from random import randint


# Hanterar felinmatning av frågor som text och kontrollerar möjliga svar
def input_valid_str(prompt, error_text, mojliga_svar):
    answer = input(prompt)
    while answer not in mojliga_svar:
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


# Sätter hur många gånger en fråga får upprepas baserat på antalet valda frågor
def max_repeated_questions(no_questions):
    if 12 <= no_questions <= 13:
        return 1
    elif 14 <= no_questions <= 26:
        return 2
    elif 27 <= no_questions <= 39:
        return 3

# Genererar en ny fråga och kontrollerar att den inte har ställts för många gånger
def get_question(table, operator, asked_question, no_questions):
    max_times = max_repeated_questions(no_questions)

    while True:
        number = randint(0, 12)
        question = f"{number}{operator}{table}"

        if asked_question.count(question) < max_times:
            asked_question.append(question)
            return question, number

# Hanterar svaret på frågan
def get_correct_answer(table, operator, number):
    if operator == '*':
        return number * table
    elif operator == '//':
        return number // table
    elif operator == '%':
        return number % table

# Huvudprogrammet, inlindat i en play_again loop för att hantera om spelaren vill spela igen
play_again = True
ask_new_settings = True
answer_scope = None
answer_table = None
answer_operator = None

while play_again:
    if ask_new_settings:
        answer_scope = input_valid_int('Hur många frågor vill du ha? (12-39 st) ', 'Ange giltigt svar!', 12, 39)
        answer_operator = input_valid_str('Vilken faktor vill du öva på? ( *, // eller %) ', 'Ange giltigt svar!', ['*', '//', '%'])
        if answer_operator in ['//', '%']:
            answer_table = input_valid_int('Välj en divisor mellan 2-5: ', 'Ange giltigt svar!', 2, 5)
            
        elif answer_operator  == '*':
            answer_table = input_valid_int('Vilken tabell vill du öva på? (2-12) ', 'Ange giltigt svar!', 2, 12)
        
    # Hanterar spelets gång och loopar samma tabell, operator och antal frågor om spelaren väljer att spela igen, ej vinst 
    keep_playing = True
    current_question = 1
    no_doors = answer_scope
    zombie_door = randint(1, no_doors)
    game_won = False
    asked_question = []

    # Loop som hanterar spelets gång, ställer frågor och hanterar dörrval
    while keep_playing and current_question <= answer_scope:
        question_text, number = get_question(answer_table, answer_operator, asked_question, answer_scope)
        answer = input_valid_int(f'Fråga {current_question} av {answer_scope}: Vad blir {question_text}?', 'Felaktig inmatning, ange ett heltal.', 0, 144)
        correct_answer = get_correct_answer(answer_table, answer_operator, number)

        # Kontrollerar svaret och hanterar dörrvalet
        if int(answer) == int(correct_answer):
            if current_question == answer_scope:
                print('Grattis, du klarade spelet!')
                keep_playing = False
                game_won = True
            else:
                chosen_door = input_valid_int(f'Vilken dörr vill du välja? (1-{no_doors}) ', f'Felaktig inmatning, välj en dörr mellan 1 och {no_doors}', 1, no_doors)

                # Kontrollerar om spelaren valde rätt dörr och uppdaterar spelet
                if chosen_door != zombie_door:
                    print('Rätt svar!')
                    print(f'Zombien var bakom dörr: {zombie_door}')
                    current_question += 1
                    no_doors -= 1
                    if no_doors >= 1:
                        zombie_door = randint(1, no_doors)
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
