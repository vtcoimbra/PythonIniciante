#entrada de dados
codVendedor = int (input("Digite o número do vendedor"))
salFixo = float (input("Informe o salário fixo"))
totVendas = float (input("Digite o total de vendas em dinheiro"))

#processamento e saida de dados

if totVendas > 100 and totVendas <= 500:
    salFinal = salFixo + 50
    print("Salário final com prêmio: ", salFinal)
elif totVendas > 500 and totVendas <= 750:
    salFinal = salFixo + 70
    print("Salário final com prêmio: ", salFinal)
elif totVendas > 750:
    salFinal = salFixo + 100
    print("Salário final com prêmio: ", salFinal)
else:
    exit()