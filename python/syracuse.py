def longueur_vol(n):
	"""retourne la longueur de vol necessaire pour atteindre 1"""
	assert type(n) == int and n >= 1
	compteur = 0
	while n > 1 :
		#print(n)
		if n % 2 == 0:
			n = n // 2
		else :
			n = n * 3 + 1
		compteur += 1
	return compteur
###########################

def syracuse(n) :
	"""retourne la liste des entiers de syracuse de n"""
	assert type(n) == int
	tableau = []
	while n >=  1 :
		if n % 2 == 0 :
			n = n / 2
		else :
			n = n * 3 + 1

		tableau.append(n)
	return tableau


#test
assert longueur_vol(3) == 7
assert longueur_vol(7) == 16
assert longueur_vol(1) == 0
assert syracuse(3) == [3, 10, 5, 16, 8, 4, 2 , 1]
assert syracuse(1) == [1]
print("caca")					

