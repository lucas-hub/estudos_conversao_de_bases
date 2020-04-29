def decToHex():
    numero_decimal = int(input("escolha um numero decimal: "))
    hexadecimal = ""
    while numero_decimal != 0:
        restante = mudaDigito(numero_decimal % 16)
        hexadecimal = str(restante) + hexadecimal
        numero_decimal = int(numero_decimal / 16)
    return print(hexadecimal)

def mudaDigito(digito):
    decimal =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for contador in range(7):
        if digito == decimal[contador - 1]: # inverte os digitos
            digito = hexadecimal[contador - 1] # inverte os digitos
    return digito

if __name__ == '__main__':
    decToHex()


