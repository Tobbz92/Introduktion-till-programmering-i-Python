from random import shuffle
nr = input('Ange heltal: ')
lst = nr.split()
lst_nr = [int(element) for element in lst]
print(f'Inmatade tal som lista: {lst_nr}')
print(f'Första talet i listan är: {lst_nr[0]}')
lst_nr.reverse()
print(f'Listan i omvänd ordning: {lst_nr}')
lst_nr.sort()
print(f'Sorterad lista: {lst_nr}')
antal = len(lst_nr)
print(f'Listan har {antal} element')
max_nr = max(lst_nr)
min_nr = min(lst_nr)
print(f'Minsta talet i listan är {min_nr} och störta talet är {max_nr}')
summa = sum(lst_nr)
antal = len(lst_nr)
medel = summa/antal
print(f'Summan av talen är {summa} och medelvärdet är {medel:.2f}')
shuffle(lst_nr)
print(f'Listan i slumpad ordning: {lst_nr}')
print(f'Det sista talet i den slumpade listan är: {lst_nr[-1]}')








