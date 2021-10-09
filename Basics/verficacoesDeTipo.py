num1 = input("Digite um numero : ")
num2 = input("Digite outro numero : ")

# Verificar numeros
# isdigit isnumeric isdecimal

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)

else:
    print("Digite um número válido"),

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 * num2)

except:
    print("Error")
