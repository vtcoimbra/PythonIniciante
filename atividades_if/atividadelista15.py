#entrada de dados
valCompra = float (input("Informe o valor da compra"))
codCliente = int (input("Digite 1 se o cliente é normal \n 2 se é especial \n e 3 se é um funcionário"))

#processamento e saida de dados

if codCliente == 1:
    print("Nenhum desconto é aplicado para esse cliente, valor total da compra: ", valCompra)

elif codCliente == 2:
    valFinal = valCompra * 0.90
    print("Cliente especial informado, desconto de 10%. Valor final da compra: ", valFinal)
elif codCliente == 3:
    valFinal = valCompra * 0.95
    print("Funcionário informado, desconto de 5%. Valor final da compra: ",  valFinal)
else:
    exit()