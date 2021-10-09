#Obter o ano de nascimento de uma pessoa ( baseado na idade e no ano atual)
#Obter o IMC da pessoa com 02 casas decimais
#Exibir um texto com todos os valores na tela
#

idade = 21
anoAtual = 2021

anoNascimento = anoAtual - idade
print(f"Você nasceu em : {anoNascimento}")

peso = 60
altura = 1.69
imc = peso / altura**2

print(f"Seu IMC é : {imc:.2f}")
