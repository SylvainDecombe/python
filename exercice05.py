def is_number_correct(number):
    t = (True, 0)

    if number < 10 and number >= 0 :
        t = (False, 10 - number)
    elif number > 20 :
        t = (False, 20 - number)
    elif number < 0 :
        t = (False, abs(number)+10)
    return t

def run():
    assert is_number_correct(0) == (False, 10)
    assert is_number_correct(10) == (True, 0)
    assert is_number_correct(20) == (True, 0)
    assert is_number_correct(21) == (False, -1)
    assert is_number_correct(50) == (False, -30)
    assert is_number_correct(15) == (True, 0)
