#entrada de dados
valProduto = float (input("Informe o valor do produto"))
quantParcela = int (input("Informe se o produto vai ser parcelado em 3 ou 5 vezes"))

#processamento de dados

if quantParcela == 3:
    valTotal = valProduto * 1.10
    valParcelado = valTotal / 3
    print("O valor final do produto é de: ", valTotal)
    print("\n E o valor das prestações são de: ", valParcelado)
elif quantParcela == 5:
    valTotal = valProduto * 1.20
    valParcelado = valTotal / 5
    print("O valor final do produto é de: ", valTotal)
    print("\n E o valor das prestações são de: ", valParcelado)
else:
    exit()