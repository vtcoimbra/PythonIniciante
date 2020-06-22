#Entrada de dados
indice = float (input("Informe o indice de poluição medido"))

#Processamento e saida de dados
if indice >= 0.3 and indice < 0.4:
    print("O grupo 1 está sendo notificado para suspender as suas atividades")
elif indice == 0.4 and indice < 0.5:
    print("O grupo 1 e 2 estão sendo notificados para suspender as suas atividades")
elif indice == 0.5:
    print("Todos os grupos estão sendo notificados para pararem suas atividades")
else:
    exit()