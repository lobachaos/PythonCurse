"""
Formatando numeros com modificadores
:s - Texto ( Strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NUMERO)f - Quantidade de casas decimais (float)
:CARACTERE (>ou < ou ^) (Quantidade) (Tipo -s. d ou f )

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2

print(f'{divisao:.2f}')

num3 = 1
print(f'{num3:0>10}')
print(f'{num3:0<5}')

nome = "Samara"
nome_formatado = '{n:@>15}'.format(n=nome)
print(nome_formatado)

nome2 = "joaozim da costa"
print(nome2.title())
