#entrada de dados

precoFab = float (input("Informe o preço de fábrica do automóvel"))

#processamento de dados
perDis = precoFab * 0.28
perImp = precoFab * 0.45

precoTot = perDis + perImp + precoFab

#saida de dados

print("O valor final do automóvel será de: ", precoTot)
