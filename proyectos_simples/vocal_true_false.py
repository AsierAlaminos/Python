vocales=["a", "e", "i", "o" ,"u"]
def vocal(letra):
    if letra in vocales:
        return True
    else:
        return False

vocal(str(input(":::")))
