idade = input("Qual sua idade ?")

if not idade.isnumeric():
    print("Digite um numero valido")
else:
    idade = int(idade)
    print("Pode acessar" if idade > 18 else "Acesso Negado") # Ternário em Python
