import random

def gen_kod():
	''' Generuje unikalny 4-ro cyfrowy ukryty kod z zakresu <1,6> '''
	ukryty_kod = ''
	zbior = [str(x) for x in range(1,6)]

	for i in range(4):
		losowa_liczba = random.choice(zbior)
		ukryty_kod += losowa_liczba
		zbior.remove(losowa_liczba)
	return ukryty_kod

def podpowiedz(wybor, kod):
	''' Sprawdzenie liczb co do pozycji i rodzaju '''
	for i in range(4):
		if wybor[i] == kod[i]:
			print ('X', end='')
			
		elif wybor[i] in kod:
			print ('O', end='')

		else:
			print ('-', end=''),
	print ('')

def runda():
	''' Wpisanie kodu oraz sprawdzanie jego poprawnosci '''
	while True:
		wybor = input('Wpisz unikalny 4-cyfrowy kod: ')
		if len(wybor) != 4:
			print ('Blad!')
		else:
			print ('Wybor:')
			print(wybor)
			return wybor


def main():
	''' Rozpoczecie gry, wygenerowanie ukrytego kodu,
	inicjacja poszczegolnych rund oraz sprawdzanie wygranej '''
	print ('Mastermind!\n')
	kod = gen_kod()
	while True:
		wybor = runda()
		if kod == wybor:
			print ('WYGRANA!')
			return
		else:
			print ('Podpowiedz:')
			podpowiedz(wybor, kod)

if __name__ == '__main__':
    main()
