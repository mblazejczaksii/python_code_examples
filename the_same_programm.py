# Usuwanie niepotrzebnych spacji ze słów podanych przez użytkownika a następnie łączenie ich ze sobą
def liczenie_slow():
    print('Podaj liczbę słów...')
    liczba_slow = input(int())
    return liczba_slow


lista_slow = []
liczba = liczenie_slow()
wynik = ''

for n in range(int(liczba)):
    print(f"Podaj słowo nr: {n + 1}")
    slowo = input()
    lista_slow.append(slowo)

print('Twoja lista słów: ', lista_slow)

for n in lista_slow:
    n = (n.rstrip()).lstrip()
    wynik = wynik + n + ' '

print('Twój wynik to: ', wynik)