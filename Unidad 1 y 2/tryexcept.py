def divide(x: float, y: float)->float:

    try:
        return x / y
    except ZeroDivisionError:
        return y / x
    #except ZeroDivisionError:
        #return "No se puede dividir entre 0"


print(divide(4, 0))