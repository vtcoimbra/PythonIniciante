#entrada de dados
quantEstoque = int (input("Informe a quantidade total de produtos no estoque no momento"))
quantPedido = int (input("Informe a quantidade de produtos no pedido"))

#processamento e saida de dados

quantRestam = quantEstoque - quantPedido

if quantEstoque < quantPedido:
    print("Não há itens suficientes para atender o pedido")
else:
    print("Ainda restam ", quantRestam, " no estoque")