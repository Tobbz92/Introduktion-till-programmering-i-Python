from random import randint


def input_valid_str(prompt, error_text, possible_answers):
    """Return a valid string input that matches one of the allowed answers."""
    answer = input(prompt)
    while answer not in possible_answers:
        answer = input(f"{error_text}\n{prompt}")
    return answer


def input_valid_int(prompt, error_text, min_value, max_value):
    """Return a valid integer input within the given range."""
    while True:
        answer = input(prompt)
        if answer.isdigit() and min_value <= int(answer) <= max_value:
            return int(answer)
        print(error_text)


def max_repeated_questions(no_questions):
    """Return how many times a question may be repeated based on total count."""
    if 12 <= no_questions <= 13:
        return 1
    if 14 <= no_questions <= 26:
        return 2
    if 27 <= no_questions <= 39:
        return 3
    return 1


def get_question(table, operator, asked_questions, no_questions):
    """Generate a new question that has not been repeated too many times."""
    max_times = max_repeated_questions(no_questions)

    while True:
        number = randint(0, 12)
        question = f"{number}{operator}{table}"

        if asked_questions.count(question) < max_times:
            asked_questions.append(question)
            return question, number


def get_correct_answer(table, operator, number):
    """Return the correct answer for the given operator and numbers."""
    if operator == "*":
        return number * table
    if operator == "//":
        return number // table
    if operator == "%":
        return number % table
    return None


def main():
    """Main game loop."""
    play_again = True
    ask_new_settings = True

    answer_scope = None
    answer_table = None
    answer_operator = None

    while play_again:
        if ask_new_settings:
            answer_scope = input_valid_int(
                "Hur många frågor vill du ha? (12–39) ",
                "Ange giltigt svar!",
                12,
                39,
            )

            answer_operator = input_valid_str(
                "Vilken faktor vill du öva på? (*, // eller %) ",
                "Ange giltigt svar!",
                ["*", "//", "%"],
            )

            if answer_operator in ["//", "%"]:
                answer_table = input_valid_int(
                    "Välj en divisor mellan 2–5: ",
                    "Ange giltigt svar!",
                    2,
                    5,
                )
            else:
                answer_table = input_valid_int(
                    "Vilken tabell vill du öva på? (2–12) ",
                    "Ange giltigt svar!",
                    2,
                    12,
                )

        keep_playing = True
        current_question = 1
        no_doors = answer_scope
        zombie_door = randint(1, no_doors)
        game_won = False
        asked_questions = []

        while keep_playing and current_question <= answer_scope:
            question_text, number = get_question(
                answer_table, answer_operator, asked_questions, answer_scope
            )

            answer = input_valid_int(
                f"Fråga {current_question} av {answer_scope}: Vad blir {question_text}? ",
                "Felaktig inmatning, ange ett heltal.",
                0,
                144,
            )

            correct_answer = get_correct_answer(answer_table, answer_operator, number)

            if answer == correct_answer:
                if current_question == answer_scope:
                    print("Grattis, du klarade spelet!")
                    keep_playing = False
                    game_won = True
                else:
                    chosen_door = input_valid_int(
                        f"Vilken dörr vill du välja? (1–{no_doors}) ",
                        f"Felaktig inmatning, välj en dörr mellan 1 och {no_doors}",
                        1,
                        no_doors,
                    )

                    if chosen_door != zombie_door:
                        print("Rätt svar!")
                        print(f"Zombien var bakom dörr: {zombie_door}")
                        current_question += 1
                        no_doors -= 1

                        if no_doors >= 1:
                            zombie_door = randint(1, no_doors)
                    else:
                        print("Rätt svar men zombien åt upp dig!")
                        keep_playing = False
            else:
                print("Fel svar!")
                keep_playing = False

        restart = input_valid_str(
            "Vill du spela igen? (j/n) ",
            "Ange giltigt svar!",
            ["j", "n"],
        )

        if restart == "n":
            print("Tack för att du spelade!")
            play_again = False
        else:
            ask_new_settings = game_won


if __name__ == "__main__":
    main()
