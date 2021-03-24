def is_product_negative(a, b):
    # Votre code ici
    return False if a >= 0 and b >= 0 or a <= 0 and b <= 0 else True

def run():
    assert is_product_negative(6, 7) == False
    assert is_product_negative(1, 0) == False
    assert is_product_negative(-1, 5) == True
    assert is_product_negative(1, -5) == True
    assert is_product_negative(-1, -5) == False
