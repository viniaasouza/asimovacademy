import os
import random

print("========================================")
print("BEM VINDO AO JOGO PEDRA PAPEL E TESOURA")
print("========================================")

placarEu = 0
placarPc = 0

pedra = 1
papel = 2
tesoura = 3


while True:
    print("placar")
    print(f"você: {placarEu}")
    print(f"computador: {placarPc}")

    print(f"Escolha entre 1-Pedra | 2-Papel | 3-Tesoura")
    
    try:
        meu = int(input()) #usuario escolhendo entre pedra papel e tesoura
        if meu not in [1,2,3]:
            print("escolha inválida")
            continue
    except ValueError:
        print("entrada invalida, por favor insira um número")
        continue
    Pc = random.choice([1,2,3])#computador escolhendo entre pedra papel e tesoura
    
    #farei um dicionario para que seja possível comparar strings e definir o vencedor por rodada
    escolhas = {1:"pedra", 2:"papel", 3:"tesoura"}
    print(f"você escolheu: {meu}")
    print(f"o computador escolheu: {Pc}")    

    if meu == Pc:
        print("empate")

    elif (meu == pedra) and (Pc == tesoura) or (meu == papel) and (Pc == pedra) or (meu == tesoura) and (Pc == papel):
        print("você ganhou!")
        placarEu += 1
    else:
        print("O computador ganhou!")
        placarPc += 1

    #condição para continuar jogando
    jogar_novamente = 1
    jogar_novamente = input("você deseja jogar novamente? 1-sim, 0-não: ")
    if jogar_novamente != 1:
        break
    print(f"placar Final: {placarEu} eu, {placarPc} Pc")
    print("Fim de jogo")

