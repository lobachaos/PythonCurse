"""
Faça um programa que peça ao usuario para digitar um número inteiro, informe se este número é par ou impar
Caso o usuário não digite um número inteiro , informe que não é um numero inteiro
"""

"""
Faça um programa que pergunta a hora ao usuário e , baseando-se no horário descrito , exiba a saudação apropriada
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

# Second Program

num2 = input("Que Horas São ? ")

num2formatado = num2.replace(':', '')
if num2formatado.isnumeric():
    num2formatado = int(num2formatado)
    if 0 <= num2formatado <= 1100:
        print("Bom dia")
    elif 1100 <= num2formatado <= 1700:
        print("Boa tarde")
    else:
        print("Boa noite")
else:
    print("Numero invalido ")

# Three Program

nome = input("Qual é seu primeiro nome ? ")
if len(nome) <= 4:
    print("O seu nome é curto")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
