import math

numero_inicial = (str(input('numero: ')))

def HexToBin():
    numero_hexadecimal = int(numero_inicial, 16)
    binario = ''
    while numero_hexadecimal != 0:
        restante = numero_hexadecimal % 2
        binario = str(restante) + binario 
        numero_hexadecimal = int(numero_hexadecimal / 2)
    return print(binario)
        

if __name__ == '__main__':
    HexToBin()

