# Funktion för att beräkna resultatet


def calculate(operand_1, operator, operand_2):
    # Kontrollerar så att korrekt räknesätt har angivits
    if operator not in ['+', '-', '*', '/', '%', '//']:
        return 'Felaktig operator'
    
    if operator in ['/', '//', '%'] and operand_2 == 0:
        return 'Error: Division med 0'

    if operator == '+':
        return operand_1 + operand_2
    if operator == '-':
        return operand_1 - operand_2
    if operator == '*':
        return operand_1 * operand_2
    if operator == '/':
        return operand_1 / operand_2
    if operator == '%':
        return operand_1 % operand_2
    if operator == '//':
        return operand_1 // operand_2


while True:
    fråga = input('Vad vill du räkna ut: ')
    
    result = None  # Återställer result för att inte skriva ut det lagrade resultatet från förra inmatningen
    
    try:
        tal_1, op, tal_2 = fråga.split()  # Delar upp indata
        # Hanterar tal som matas in med fel format och omvandlar till flyttal
        tal_1 = float(tal_1.replace(',', '.'))  
        tal_2 = float(tal_2.replace(',', '.'))
        
    # Hanterar fel antal delar, fel operator och felaktig operand
    except ValueError:
        print('Felaktig inmatning')
        result = None  # Återställer result för att inte skriva ut det lagrade resultatet från förra inmatningen
        
    else:
        result = calculate(tal_1, op, tal_2)
    
    if result is not None:
        if isinstance(result, str):
            # Skriver ut felmeddelande om result är en text
            print(result)
        else:
            # Om result inte är en text skrivs detta ut
            print(f'{tal_1} {op} {tal_2} = {result}')
