#entrada de dados
sal = float (input("Informe o seu salário"))
prest = float (input("Informe o valor da prestação"))


#processamento de dados

if prest > sal * 0.20:
    print("Empréstimo não pode ser concedido!")