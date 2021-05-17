def esPrimo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return esPrimo(num, n+1)
    else:
        print("No es primo",n,"es divisor")
        return False

'''
if esPrimo(546546):
    print("Te invito a comer")
else:
    print("Tu me invitas a comer")
'''
