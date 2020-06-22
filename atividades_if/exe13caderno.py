# entrada de dados
hinicio = int(input("Digite a hora que o jogo começará (sem os minutos):"))
minicio = int(input("Digite os minutos referentes ao inicio do jogo: "))

hfinal = int(input("Digite a hora que o jogo terminará (sem os minutos):"))
mfinal = int(input("Digite os minutos referentes ao fim do jogo: "))

# processamento de dados
if hinicio >= hfinal:
    hfinal
