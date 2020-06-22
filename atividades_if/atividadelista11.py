#entrada de dados
numVend = int (input("Digite o seu número de vendedor"))
salFixo = float (input("Digite seu salário fixo"))
totVend = float (input("Informe o total de vendas realizadas em dinheiro"))
perVend = float (input("Informe o percentual do total de vendas (somente números)"))

#processamento de dados

salAd = totVend * perVend / 100
salTot = salFixo + salAd

#saida de dados

print("vendedor:", numVend)
print("Salário total do vendedor: ", salTot)