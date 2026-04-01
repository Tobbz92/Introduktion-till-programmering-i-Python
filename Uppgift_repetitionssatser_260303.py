fortsätt = 'j'
while fortsätt == 'j':
    antal = 0
    summa = 0
    tal = int(input('Ange ett positivt heltal: '))
    while tal != 0:
        if tal < 0:
            print('Negativa tal inkluderas inte i summan!')
        else:
            antal = antal + 1      
            summa = summa + tal    
        tal = int(input('Ange ett positivt heltal: '))
    if antal != 0:
        medelvärde = summa / antal
        print('Summan av de inmatade talen är:', summa)
        print('Medelvärdet är:', medelvärde)
    else:
        print('Du har inte skrivit in några tal')
    
    fortsätt = input('\nVill du fortsätta (j/n)? ')   
print('Programmet avslutas!') 
