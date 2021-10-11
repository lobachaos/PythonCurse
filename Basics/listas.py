lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[::-1])  # Forma prática de inverter a ordem
print(lista[::2])
print(lista[0:2])

del (lista[3:5])  # Ultimo não entra , nesse caso indice 5
print(lista)

# Outra forma de criar uma lista

l1 = list(range(0, 10))
print(f"Nova lista >> {l1}")

secreto = "som"
digitados = []
revelado = False
tentativas = 5

while not revelado and tentativas != 0:
    letra = input("Digite uma letra : ").lower()

    if len(letra) > 1:
        print("Insira somente UMA letra !")
        continue
    digitados.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" está na palavra secreta')
    else:
        print(f'a letra "{letra}" NÃO está na palavra secreta')
        digitados.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    print(secreto_temp)

    if secreto_temp == secreto:
        revelado = True
        print(f"Você acertou a palavra secreta {secreto} !! ")
    else:
        print(f'A palavra está assim : "{secreto_temp}"')
        tentativas -= 1
        print(f'Você possui {tentativas} tentativas')
        if tentativas == 0:
            print("Voce perdeu :(")
