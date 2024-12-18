import random
import seaborn as sns

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10,100) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()


    def reiniciar_o_dia(self):
        self.porta_halteres = {i:i for i in self.halteres}
    def listar_halteres(self):
        return [i for i  in list(self.porta_halteres.values()) if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        halt_keys = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[halt_keys] = 0
        return peso

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo # tipo 1 normal e tipo 2 bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        if lista_pesos:
            self.peso = random.choice(lista_pesos)
            self.academia.pegar_haltere(self.peso)
        else:
            self.peso = 0

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
                
        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)
        self.peso = 0

academia = Academia()       

usuarios = [Usuario(1,academia)for i in range(20)]
usuarios += [Usuario(2,academia)for i in range(1)]
random.shuffle(usuarios)

list_chaos = []

for k in range(50):
    academia.reiniciar_o_dia()                    
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_chaos += [academia.calcular_caos()]
print(list_chaos)



sns.displot(list_chaos)