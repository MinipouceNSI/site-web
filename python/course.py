
def nombre_coureurs(lst) :
	"""
	retourne le nombre de coureur dans la liste
	"""
	assert type(lst) == list
	assert all([type(obj) == str for obj in lst])
	n = 0
	for elt in lst:
		n += 1
	return n
#######################
def premier(lst):
	"""retourne premier coureur de la liste"""
	assert type(lst) == list
	assert all([type(obj) == str for obj in lst])
	return lst[0]

########################
def dernier(lst):
	"""retourne le dernier de la liste"""
	assert type(lst) == list
	assert all([type(obj) == str for obj in lst])
	return lst[len(lst) - 1]
##########################
def coureur_en_position(lst, position):
	"""retourne le coureur en fonction de position"""
	assert type(lst) == list
	assert type(position) == int and position >= 1 and position <= len(lst)
	assert all([type(obj) == str for obj in lst])
	return lst[position - 1]



#test
classement = ["Nadia", "Paul", "Titouan", "Louane", "Evan"]
assert nombre_coureurs(classement) == 5
assert premier(classement) == "Nadia"
assert dernier(classement) == "Evan"
assert coureur_en_position(classement, 3) == "Titouan"
print("caca")
