import random

mise = -1
numero = -1
roulette = range(49)
result = random.randint(0, 49)

while int(mise) < 0 :
    mise = input("Veuillez saisir une somme à miser : ")
while int(numero) < 0 or int(numero) > 49 :
    numero = input("Veuillez saisir une valeur enter 0 et 49 : ")

print(f"Vous avez misé {mise} euros sur le {numero}" )
print(f"Le numéro gagnant est : {result}")

numero = int(numero)
mise = int(mise)

if numero == result :
    gain = mise*3
    print(f"Vous avez gagné {gain} euros !!")
elif (numero % 2) == 0 and (result % 2) == 0 :
    gain = mise/2
    print(f"Vous avez gagné {gain} euros !!")
elif (numero % 2) != 0 and (result % 2) != 0 :
    gain = mise/2
    print(f"Vous avez gagné {gain} euros !!")
else :
    print("Vous avez perdu voter mise !")
