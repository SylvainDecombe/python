import random
import re

liste_mots = ['kayak', 'voiture', 'chaise', 'appartement', 'bateau', 'table', 'ordinateur']
lettre = '.'

while re.search("[a-zA-Z]", lettre) == False :
    lettre = input("Veuillez saisir une lettre : ")

print(f"{lettre}")
