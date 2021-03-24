def get_category(age):
    categorie = ''
    if(age > 5 and age < 8) :
        categorie = 'Poussin'
    elif (age > 7 and age < 10) :
        categorie = 'Pupille'
    elif (age > 9 and age < 12) :
        categorie = 'Minime'
    elif (age > 11) :
        categorie = 'Cadet'
    return categorie

def run():
    assert get_category(6) == "Poussin"
    assert get_category(7) == "Poussin"
    assert get_category(8) == "Pupille"
    assert get_category(9) == "Pupille"
    assert get_category(10) == "Minime"
    assert get_category(11) == "Minime"
    assert get_category(12) == "Cadet"
    assert get_category(99) == "Cadet"
    
    try:
        get_category(1)
        raise ValueError()
    except ValueError:
        pass
