# Funktion för att beräkna resultatet


def calculate(operand_1, operator, operand_2):
    # Hanterar division med 0
    if operator in ['/', '%', '//'] and operand_2 == 0:
        return 'Error: Division med 0'
    
    # Kontrollerar så att korrekt räknesätt har angivits
    if operator not in ['+', '-', '*', '/', '%', '//']:
        return 'Felaktig operator!'
    
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '/':
        return operand_1 / operand_2
    elif operator == '%':
        return operand_1 % operand_2
    elif operator == '//':
        return operand_1 // operand_2


while True:
    fråga = input('Vad vill du räkna ut: ')
    tal_1, op, tal_2 = fråga.split()  # Delar upp indata
    tal_1 = float(tal_1)
    tal_2 = float(tal_2)

    result = calculate(tal_1, op, tal_2)
    
    if isinstance(result, str):
        # Skriver ut felmeddelande om result är en text
        print(result)
    else:
        # Om result inte är en text skrivs detta ut
        print(f'{tal_1} {op} {tal_2} = {result}')
