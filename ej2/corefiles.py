def ValidInt():
    try:
        n = int(input(')..'))
    except ValueError:
        return ValidInt()
    else:
        return n
    
def ValidFloat():
    try:
        n = float(input(')..'))
    except ValueError:
        return ValidFloat()
    else:
        return n

def Validstr():
    n = input(')..')
    if(bool(n) == True):
        return n
    else:
        return Validstr()