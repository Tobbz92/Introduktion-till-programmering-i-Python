avsluta = 'n'
while avsluta == 'n':
    tabell = int(input('Ange tabell: '))
    start = int(input('Ange startintervall: '))
    stopp = int(input('Ange stoppintervall: '))
    stopp = stopp + 1
    print('----------------------')
    print(f'{tabell}:ans tabell')
    print('----------------------')
    for tal in range(start,stopp):
        print(f'{tal:2} * {tabell:1} = {tal*tabell:3}')
    avsluta = input('\nVill du avsluta (j/n)? ').lower()
    while avsluta not in ('n', 'j'):
        print('Felaktigt svar')
        avsluta = input('\nVill du avsluta (j/n)? ').lower()
print('Programmet avslutas!')
