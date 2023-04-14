import fabrica_dados as fd
import random

class Rota():
    #Inicia o individuo com uma rota aleatoria
    def __init__(self, dados: fd.FabricaDados, rota = None):
        self.dados = dados
        self.rota = rota
        if rota == None:
            self.rota = self.gerar_rota()
        self.fitness_val = self.fitness()

    def __str__(self):
        return ', '.join(self.rota)

    def gerar_rota(self):
        rota = []
        cidades = self.dados.cidades
        randon_list = random.sample(range(len(cidades)), len(cidades))
        rota.append('Escondidos')
        for i in range(13):
            rota.append(cidades[randon_list[i]])
        return rota

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
        
        #Verificar se há cidades repetidas na rota sem contar a primeira
        temp_arr = rota[1:]
        if len(temp_arr) != len(set(temp_arr)):
            return float('-inf')

        for i in range(len(rota)):
            #Verificar as restrições antes para economizar processamento
            if peso_total > 20:
                return float('-inf') # Retorna -inf caso a rota exceda o limite de peso
            if tempo_total > 72:
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
                        #Se a cidade não tiver item, retorna -inf (só Escondidos não está na lista)
                        return valor_total - custo_transporte 
                except KeyError: 
                    return float('-inf') # Retorna -inf caso a rota não seja válida
    
    #muda aleatoriamente a ordem de duas cidades com exceção da primeira
    def mutacao(self):
        rota = self.rota
        randon_list = random.sample(range(1, len(rota)), 2)
        rota[randon_list[0]], rota[randon_list[1]] = rota[randon_list[1]], rota[randon_list[0]]
        return Rota(self.dados, rota)
        
