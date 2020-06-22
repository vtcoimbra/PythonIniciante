salConta = float (input("Digite o saldo atual da conta"))
cheque1 = float (input("Digite o valor do primeiro cheque"))
cheque2 = float (input("Digite o valor do segundo cheque"))
cheque3 = float (input("Digite o valor do terceiro cheque"))

if salConta - cheque1 > 0:
    print("Primeiro cheque pago com sucesso")
    salConta2 = salConta - cheque1
    if salConta2 - cheque2 > 0:
         print("Segundo cheque pago com sucesso")
         salConta3 = salConta2 - cheque2
         if salConta3 - cheque3 > 0:
             print("Terceiro cheque pago com sucesso")
         else:
             print("Não há saldo suficiente para pagamento")
             exit()
    else:
        print("Não há saldo suficiente para pagamento")
        exit()
else:
    print("Não há saldo suficiente para pagamento")
    exit()
