from algoritmo_genetico import Individuo
import fabrica_dados as fd
import random

class Rota(Individuo):
    #Inicia o individuo com uma rota aleatoria
    def __init__(self, dados: fd.FabricaDados):
        self.rota = []
        self.dados = dados
        self.fitness_val = 0

        cidades = self.dados.cidades
        randon_list = random.sample(range(len(cidades)), len(cidades))
        self.rota.append('Escondidos')
        for i in range(13):
            self.rota.append(cidades[randon_list[i]])

    def __str__(self):
        return self.rota

    def fitness(self):
        itens = self.dados.itens
        viagens = self.dados.viagens
        rota = self.rota

        tempo_total = 0
        valor_total = 0
        peso_total = 0
        custo_transporte = 0

        if rota[0] != "Escondidos":
            return float('-inf')

        for i in range(len(rota)):
            #Verificar as restrições antes para economizar processamento
            if peso_total > 20:
                self.fitness_val = float('-inf')
                return float('-inf') # Retorna -inf caso a rota exceda o limite de peso
            if tempo_total > 72:
                self.fitness_val = float('-inf')
                return float('-inf') # Retorna -inf caso a rota exceda o limite de tempo
            if i == 0:
                continue # Ignora a primeira cidade da rota, que sempre é "Escondidos"
            else:
                try:
                    # Soma os tempos e custos de transporte
                    tempo_total += viagens[rota[i-1]][rota[i]]['tempo']
                    custo_transporte += viagens[rota[i-1]][rota[i]]['custo']
                    if rota[i] in itens:
                        tempo_total += itens[rota[i]]['tempo']
                        valor_total += itens[rota[i]]['valor']
                        peso_total += itens[rota[i]]['peso']
                    else:
                        self.fitness_val = valor_total - custo_transporte 
                        return valor_total - custo_transporte 
                except KeyError: 
                    self.fitness_val = float('-inf')
                    return float('-inf') # Retorna -inf caso a rota não seja válida

    def mutacao(self):
        #muda aleatoriamente a ordem de duas cidades
        cidades = self.dados.cidades
        randon_list = random.sample(range(len(cidades)), 2)
        self.rota[randon_list[0]], self.rota[randon_list[1]] = self.rota[randon_list[1]], self.rota[randon_list[0]]
 
    def crossover(self):
        raise NotImplementedError("Implementar")



indTeste = Rota(fd.FabricaDados())

print(indTeste.fitness())