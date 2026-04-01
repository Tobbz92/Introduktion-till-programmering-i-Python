def print_max(a, b, c):
    if a >= b and a >= c:
        störst = a
    elif b >= a and b>= c:
        störst = b
    else:
        störst = c
    print(f'Det största talet är {störst}')
    
a = int(input('Skriv in tal 1: '))
b = int(input('Skriv in tal 2: '))
c = int(input('Skriv in tal 3: '))

print_max(a, b, c)

