#   Na funcao input sempre será armazenado por padrão um tipo String

nome = input("Insira seu nome : ")
idade = input("Quantos anos você tem ? ")
anoAtual = input("Em que ano estamos ? ")

anoNascimento = int(anoAtual) - int(idade) # Cast do tipo String para Int

print(f"{nome} tem {idade} anos e nasceu no ano {anoNascimento}")