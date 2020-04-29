def decToBin():
    numero_decimal = int(input('insira seu numero decimal: '))
    binario = ''
    while numero_decimal != 0:
        restante = numero_decimal % 2
        binario = str(restante) + binario
        numero_decimal = int(numero_decimal / 2)
    return print(binario)

if __name__ == '__main__':
    decToBin()