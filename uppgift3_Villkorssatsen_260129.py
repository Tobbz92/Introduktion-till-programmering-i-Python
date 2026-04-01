resultat = int(input('Ange resultat: '))
if resultat < 0 or resultat > 50:
    betyg = 'Fel'
elif resultat >=48:
    betyg = 'A'
elif resultat >=40:
    betyg = 'B'
elif resultat >=32:
    betyg = 'C'
elif resultat >=24:
    betyg = 'D'
elif resultat >=16:
    betyg = 'E'
else:
    betyg = 'F'
if betyg == 'Fel':
    print('Felaktigt resultat!')
else:
    print('Betyget är:', betyg)