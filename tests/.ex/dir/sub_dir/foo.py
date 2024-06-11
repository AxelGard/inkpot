import math

def inverse_sqrt(x:int):
    """ a normal inverse square root """
    assert x != 0, "x must not be equal to zero"
    return 1 / math.sqrt(x)