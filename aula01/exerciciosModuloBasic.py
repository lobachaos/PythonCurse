"""
Faça um programa que peça ao usuario para digitar um número inteiro, informe se este número é par ou impar
Caso o usuário não digite um número inteiro , informe que não é um numero inteiro
"""

"""
Faça um programa que pergunta a hora ao usuário e , baseando-se no horário descritoi , exiba a saudação apropriada
Ex : Bom dia -> 0-11 , Boa Tarde -> 12-17 e Boa noite -> 18-23
"""
"""
Faça um Programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"
se tiver entre 5 e 6 letras , "Seu nome é normal " ; maior que 6 "Seu nome é mt grande "
"""

# First Program

num = input("Digite um número ")

if num.isnumeric():
    num = int(num)
    if num % 2 == 0 or num == 0:
        print("Número PAR")
    else:
        print("Número IMPAR")
else:
    print("Número invalido")
