salConta = float (input("Digite o saldo atual da conta"))
cheque1 = float (input("Digite o valor do primeiro cheque"))
if salConta - cheque1 >= 0:
    print("Primeiro cheque pago")
else:
    print("Não há saldo suficiente para pagamento")
    exit()

salConta2 = salConta - cheque1

cheque2 = float (input("Digite o valor do segundo cheque"))

if salConta2 - cheque2 >= 0:
    print("Segundo cheque pago")
else:
    print("Não há saldo suficiente para pagamento")
    exit()

salConta3= salConta2 - cheque2

cheque3 = float (input("Digite o valor do terceiro cheque"))

if salConta3 - cheque3 >= 0:
    print("Terceiro cheque pago.")
else:
    print("Não há saldo suficiente para pagamento")
    exit()