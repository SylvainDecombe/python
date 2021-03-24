a = 1
b = 2

# Votre code ici
b,a = a,b

def run():
    assert a == 2
    assert b == 1
