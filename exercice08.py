import re

def get_word_count(sentence):
       phrase = sentence.split()
       x = 0
       for word in phrase :
              if re.search("[a-zA-Z]", word) :
                     x += 1
       return x

def run():
   assert get_word_count("Bonjour") == 1
   assert get_word_count("Bonjour toi") == 2
   assert get_word_count("Bonjour ca va ?") == 3
   assert get_word_count("Bonjour ca va toi ?!") == 4
   assert get_word_count("") == 0
