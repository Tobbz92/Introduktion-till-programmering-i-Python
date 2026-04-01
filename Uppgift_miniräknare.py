fortsätt = 'j'
while fortsätt == 'j':
    operand1 = int(input('Ange operand: '))
    raknesatt = input('Ange räknesätt:')
    while raknesatt not in ['+','-','*','/','%','//']:
        print('Felaktigt räknesätt')
        raknesatt = input('Ange räknesätt')
    operand2 = int(input('Ange operand: '))
    while raknesatt in ['/', '//', '%'] and operand2 == 0:
        operand2 = int(input('Ange operand: '))
        
    if raknesatt == '+':
        svar = operand1 + operand2
    elif raknesatt == '*':
        svar = operand1 * operand2
    elif raknesatt == '-':
        svar = operand1 - operand2
    elif raknesatt == '/':
        svar = operand1 / operand2
    elif raknesatt == '//':
        svar = operand1 // operand2
    elif raknesatt == '%':
        svar = operand1 % operand2
    else:
        print('Felaktig inmatning')
    print(f'Svar: {operand1} {raknesatt} {operand2} = {svar}')
    
    fortsätt = input('Vill du fortsätta (j/n)? ').lower()
    while fortsätt not in ['j', 'n']:
        print('Felaktig inmatning')
        fortsätt = input('Vill du fortsätta (j/n)? ')
        
print('Programmet avslutas!')