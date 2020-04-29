import math

numero_inteiro_decimal = int(input('insira seu numero inteiro aqui: '))


def paraBinario():
    numero_decimal = numero_inteiro_decimal
    binario = ''
    while numero_decimal != 0:
        restante = numero_decimal % 2
        binario = str(restante) + binario
        numero_decimal = int(numero_decimal / 2)
    return print(binario)


def paraHexadecimal():
    numero_decimal = numero_inteiro_decimal
    hexadecimal = ""
    while numero_decimal != 0:
        restante = mudaDigito(numero_decimal % 16)
        hexadecimal = str(restante) + hexadecimal
        numero_decimal = int(numero_decimal / 16)
    return print(hexadecimal)


def mudaDigito(digito):
    decimal = [10, 11, 12, 13, 14, 15]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for contador in range(7):
        if digito == decimal[contador - 1]:  # inverte os digitos
            digito = hexadecimal[contador - 1]  # inverte os digitos
    return digito


def paraOctal():
    numero_decimal = numero_inteiro_decimal
    octal = ''
    while numero_decimal != 0:
        restante = numero_decimal % 8
        octal = str(restante) + octal
        numero_decimal = int(numero_decimal / 8)
    return print(octal)


print("""escolha a base de para conversao: 
1) para binária
2) para hexadecimal
3) para octal""")

opcao = int(input('sua opção: '))

if __name__ == '__main__':
    if opcao == 1:
        paraBinario()
    elif opcao == 2:
        paraHexadecimal()
    elif opcao == 3:
        paraOctal()
