import math

def factorial(number):
    if number<0 :
        result = -math.factorial(abs(number))
    else :
        result = math.factorial(number)
    return result

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320
