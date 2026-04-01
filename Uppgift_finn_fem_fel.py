from random import randint


# Funktion som slumpar fram ett antal kast till en lista
def slumpa_tärningskast_till_lista(antal_kast, lista):
    for i in range(antal_kast):
        tärningskast = randint(1, 6)
        lista.append(tärningskast)

        
# Funktion som beräknar medelvärdet på tal i en lista
def beräkna_medelvärde(lista):
    summa = 0
    for element in lista:
        summa = summa + element
    medelvärde = summa / len(lista)
    return medelvärde


def main():  # Huvudprogrammet
    # Fråga användaren om indata
    antal_kast = int(input('Hur många tärningskast vill du göra? '))

    # Skapa en tom lista
    lista = list()

    # Anropa funktionen som slumpar fram tärningskast till en lista
    slumpa_tärningskast_till_lista(antal_kast, lista)

    # Anropa funktionen som beräknar medelvärdet för elementen i en lista
    medel_värde = beräkna_medelvärde(lista)
    # Skriv ut medelvärdet
    print(f'Medelvärdet av tärningskasten är: {medel_värde:.2f}')

    # Skriv ut en frekvenstabell
    summa_tärningskast = 0
    for i in range(1, 7):
        antal = lista.count(i)
        summa_tärningskast += antal
        print(f'Antal {i}:or = {antal}')  

    # print-satsen nedan är korrekt, ändra inte den!
    print(f'Totalt antal summerade tärningskast är {summa_tärningskast}')


main()  # Anropa huvudprogrammet