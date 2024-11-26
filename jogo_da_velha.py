class Jogador: #gerenciando o estado do jogo
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

class Jogo:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)]for _ in range(3)]#criando um tabuleiro 3x3, lembrando conceito de matrizes que ja vi em C
        self.jogador_atual = None
        self.jogadores = []

    def print_tabuleiro(self):
        for row in self.tabuleiro:#irá percorrer a linhas inicilizando os elementos do tabuleiro
            print("|".join(row))#vai colocar uma coluna para cada linha
            print("-"*5) #imprime uma linha divisória de 5 itens

    def check_vencedor(self, jogador):
        for row in self.tabuleiro: #percorre todas as linhas do tabuleiro, sabendo que foi instanciado uma linha de 3 la em cima
            if all([cell == jogador.simbolo for cell in row]):  #quando percorrer ele irá conferir se os simbolos das celulas são iguais, se checar e forem iguais, retorna True e assim temos um ganhador
                return True
        for col in range(3): #não foi definido coluna, então iremos trabalhar com o range(3) para saber quanto percorrer na coluna
            if all([self.tabuleiro[row][col] == jogador.simbolo for row in range(3)]): #aqui ele irar percorrer toda a coluna até o tamanho de 3(0,1,2) e fazer a mesma verificação
                return True #se iguais retorna True e da um vencedor
        if all([self.tabuleiro[i][i] == jogador.simbolo for i in range(3)]) or all([self.tabuleiro[i][2-i] == jogador.simbolo for i in range(3)]):
            return True #o simbolo da posição (0,0),(2,2),(1,1) são iguais, vence ou || (2,(2-1=0)),(1,2-1=1)), (0,(2-0=2)) são iguais, desenhar em papel para entender melhor
        return False
    
    def tabuleiro_cheio(self):
        for row in self.tabuleiro: #percorre todas as linhas do tabuleiro
            if " " in row: #se algum estiver vazio
                return False #retornar False e continua o jogo
        return True #se não, retorna True e acaba o jogo
    
    def alternar_jogador(self):
        self.jogador_atual = self.jogadores[1] if self.jogador_atual == self.jogadores[0] else self.jogadores[0]

    def Jogar(self):
        self.jogador_atual = self.jogadores[0] #define o jogador inicial como o 0
        while True:
            self.print_tabuleiro()
            try:
                row = int(input("{}, escolhar uma linha de (0-2): ".format(self.jogador_atual.nome))) 
                col = int(input("{}, escolhar uma coluna de (0-2): ".format(self.jogador_atual.nome)))#essas duas linhas estão escolhendo as coordenadas do x ou o
                if row not in range(3) or col not in range(3):
                    print("coordenadas inválidas! escolha 0 ou 2.")
                    continue
            except ValueError:
                print("entrada invalida! Insira numero inteiro.")
                continue
            if self.tabuleiro[row][col] == " ": #verifica se esta disponivel
                self.tabuleiro[row][col] = self.jogador_atual.simbolo #aloca o simbolo na posicão disponivel
                if self.check_vencedor(self.jogador_atual): #verifica se o jogar ele vence
                    self.print_tabuleiro() # printa o tabuleiro
                    print("{}, venceu!!!".format(self.jogador_atual.nome)) #aponta o ganhador
                    break
                if self.tabuleiro_cheio(): #vai dizer se o tabuleiro vai estar cheio
                    self.print_tabuleiro() #printa o tabuleiro e printa empate
                    print("Empate")
                    break
                self.alternar_jogador() #alternar os jogadores
            else:
                print("posição já ocupada, tente novamente!")
def main():
    jogador1 = Jogador("jogador 1", "X") #atribuindo o jogador 1 como X e o 2 como O
    jogador2 = Jogador("jogador 2", "O")
    jogo = Jogo() #criando o objeto jogo
    jogo.jogadores = [jogador1, jogador2] #atribuindo os jogadores a lista
    jogo.Jogar()    #inicia o jogo

if __name__ == "__main__":
    main()