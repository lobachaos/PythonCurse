frase = "o rato roeu a roupa do rei de roma"

tamanho_frase = len(frase)
# print(tamanho_frase)

contador = 0
nova_string = ''
letra_maiscula = input("Qual letra deseja deixar maiuscula ?").lower()

while contador < tamanho_frase:
    letra = frase[contador]
    if frase.__contains__(letra_maiscula) and letra_maiscula.isalpha() is True:
        if letra == letra_maiscula:
            nova_string += letra.upper()
        else:
            nova_string += letra
    else:
        print("Letra invalida")
        break

    contador += 1

print(nova_string)
