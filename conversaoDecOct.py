def decToOct():
    numero_decimal = int(input('insira seu numero decimal: '))
    octal = ''
    while numero_decimal != 0:
        restante = numero_decimal % 8
        octal = str(restante) + octal
        numero_decimal = int(numero_decimal / 8)
    return print(octal)

if __name__ == '__main__':
    decToOct()