import re

def get_letter_count(word):
       x = 0
       for lettre in word :
              if re.search("[a-zA-Z]", lettre) :
                     x += 1       
       return x

def run():
   assert get_letter_count("Oui") == 3
   assert get_letter_count("Bonjour") == 7
   assert get_letter_count("") == 0
   assert get_letter_count(".........hein???") == 4
   assert get_letter_count("Attention y'a quatre mots !") == 21
