# Funktion för att beräkna resultatet


def calculate(operand_1, operator, operand_2):
    # Kontrollerar så att korrekt räknesätt har angivits
    if operator not in ['+', '-', '*', '/', '%', '//']:
        return 'Felaktig operator'
    
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
    
    try:
        tal_1, op, tal_2 = fråga.split()  # Delar upp indata
        # Hanterar tal som matas in med fel format och omvandlar till flyttal
        tal_1 = float(tal_1.replace(',', '.'))  
        tal_2 = float(tal_2.replace(',', '.'))

        result = calculate(tal_1, op, tal_2)
        
        if isinstance(result, str):
            # Skriver ut felmeddelande om result är en text
            print(result)
        else:
        # Om result inte är en text skrivs detta ut
            print(f'{tal_1} {op} {tal_2} = {result}')
    # Hanterar division med 0
    except ZeroDivisionError:
        print('Error: Division med 0')
    # Hanterar fel antal delar, fel operator och felaktig operand
    except ValueError:
        print('Felaktig inmatning')
