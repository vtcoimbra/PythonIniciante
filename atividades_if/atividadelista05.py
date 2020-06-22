#entrada de dados
n1 = int (input("Digite 1 para calcular a área da circunferência \n"
                "Digite 2 para calcular o perímetro da circunferência"))
r = float (input("Informe o raio da circunferência"))
a = float
p = float

#processamento e saida de dados

if n1 == 1:
    a= 3.14*(r*r)
    print("A área da circunfêrencia é igual a: ", a)
elif n1 == 2:
    p= (2*3.14)*r
    print("O perímetro da circunferência é igual a: ", p)
else:
    print("Indicadores de operação mal fornecidos. Tente novamente")