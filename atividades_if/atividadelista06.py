#entrada de dados
a = float (input("Informe o primeiro lado do triangulo"))
b = float (input("Informe o segundo lado do triangulo"))
c = float (input("Informe o terceiro lado do triangulo"))

#processamento e saída de dados

if a > b + c :
    print("Não é um triangulo retangulo")
else:
    print("É um triangulo retangulo")