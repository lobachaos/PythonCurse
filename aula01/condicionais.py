num1 = int(input("Insira um numero : "))
num2 = int(input("Insira um outro numero : "))

if num1 > num2 :
    print(f"{num1} é o maior")
elif num1 == num2 : #elif é abreviacao de else if
    print("Os números são identicos.")
else :
    print(f"{num2} é o maior")