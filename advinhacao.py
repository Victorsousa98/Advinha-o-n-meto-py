import random

print("*************************")
print("Bem vindo")
print("*************************")


numero_sorteado = random.randrange(1, 101) 
numeroSecreto = round(numero_sorteado) 
total_de_tentativas = 0
pontos = 1000

print("Nivel de dificuldade: \n [1] Fácil; [2] Médio; [3] Difícil.")

nivel = int(input("Escolha: "))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5



for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
    print("Pontos {}" .format(pontos))
    chute_str = input("Um numero de 1 a 100: ")
    chute_Int = int(chute_str)
    acertou = (chute_Int == numeroSecreto)
    chutou_um_numero_menor = (chute_Int < numeroSecreto)
    chutou_um_numero_maior = (chute_Int > numeroSecreto)


    if (chute_Int < 1 or chute_Int > 100 ):
        print("Você deve digitar um número de 1 à 100")
        continue    


    if(acertou):
        print("Você acertou!")
        print("Você fez {} pontos!" .format(pontos))
        break
    else:
        if(chutou_um_numero_maior):
            print("Você errou!")
            print("seu chute foi maior que o Numero Secreto")
        if(chutou_um_numero_menor):
            print("Você errou!")
            print("seu chute foi menor que o Numero Secreto")
        pontos_perdidos = abs(numeroSecreto - chute_Int)
        pontos = pontos - pontos_perdidos


print("O número era: ", numeroSecreto)
print("****FIM****")