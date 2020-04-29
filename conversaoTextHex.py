import binascii

def textoParaHex(text):
    encode = binascii.hexlify(bytes(text, "utf-8"))
    encode = str(encode).strip('b')
    encode = str(encode).strip("'")
    return print(encode)

if __name__ == "__main__":
    frase = str(input('insira seu texto aqui: '))
    textoParaHex(frase)

