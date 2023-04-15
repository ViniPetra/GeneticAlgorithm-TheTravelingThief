import fabrica_dados as fd
import random

class Rota():
    #Inicia o individuo com uma rota aleatoria
    def __init__(self, dados: fd.FabricaDados, rota = None):
        self.dados = dados
        self.rota = rota
        if rota == None:
            self.rota = self.gerar_rota()
        self.peso = 0
        self.tempo_total = 0

    def __str__(self):
        string = f"fitness: {self.fitness()}\nstatus: {self.status}\nrota: {self.rota}\npeso: {self.peso}\ntempo: {self.tempo_total}"
        return string

    def gerar_rota(self):
        rota = []
        cidades = self.dados.cidades
        randon_list = random.sample(range(len(cidades)), len(cidades))
        rota.append('Escondidos')
        for i in range(13):
            rota.append(cidades[randon_list[i]])
        return rota
    

    #muda aleatoriamente a ordem de duas cidades com exceção da primeira
    def mutacao(self):
        rota = self.rota
        randon_list = random.sample(range(1, len(rota)), 2)
        rota[randon_list[0]], rota[randon_list[1]] = rota[randon_list[1]], rota[randon_list[0]]
        return Rota(self.dados, rota)
        

    #-----------------Funções de fitness-----------------


    # Verifica se a rota é válida
    def rota_valida(self):
        # Verifica se a primeira cidade é Escondidos
        if self.rota[0] != "Escondidos":
            self.status = 'Rota inválida: a primeira cidade não é Escondidos'
            return False
        
        # Verifica se Escondidos aparece pelo menos duas vezes
        if self.rota.count('Escondidos') < 2:
            self.status = 'Rota inválida: Escondidos não aparece duas vezes'
            return False

        # Verifica se Escondidos não é a segunda cidade da rota
        if self.rota[1] == 'Escondidos':
            self.status = 'Rota inválida: Escondidos é a segunda cidade da rota'
            return False
        
        # Cria a sub-rota válida
        sub_rota = []
        i = 1
        while self.rota[i] != 'Escondidos':
            sub_rota.append(self.rota[i])
            i += 1
        
        # Verifica se a sub-rota possui cidades repetidas
        if len(sub_rota) != len(set(sub_rota)):
            self.status = 'Rota inválida: a sub-rota possui cidades repetidas'
            return False
        
        return True
    
    def cria_sub_rota(self):
        sub_rota = []
        i = 1
        while self.rota[i] != 'Escondidos':
            sub_rota.append(self.rota[i])
            i += 1
        return sub_rota

    # Retorna o valor total obtido na rota
    def valor_total(self):
        itens = self.dados.itens

        sub_rota = self.cria_sub_rota()

        # Soma o valor total dos itens da sub-rota
        valor_total = 0
        for cidade in sub_rota:
            if cidade in itens:
                valor_total += itens[cidade]['valor']
            else:
                raise Exception(f"Cidade '{cidade}' não está na lista de itens.")

        return valor_total
            
    # Retorna o tempo total da rota
    def peso_total(self):
        itens = self.dados.itens

        sub_rota = self.cria_sub_rota()

        # Soma o peso total dos itens da sub-rota
        peso_total = 0
        for cidade in sub_rota:
            if cidade in itens:
                peso_total += itens[cidade]['peso']
            else:
                raise Exception(f"Cidade '{cidade}' não está na lista de itens.")
        self.peso = peso_total
        return peso_total
    
    # Cria uma lista com a rota entre Escondidos e contando ambos
    def cria_rota_efetiva(self):
        rota_efetiva = []
        i = 1
        rota_efetiva.append(self.rota[0])
        while self.rota[i] != 'Escondidos':
            rota_efetiva.append(self.rota[i])
            i += 1
        rota_efetiva.append(self.rota[i])
        
        return rota_efetiva

    # Retorna o tempo total da rota
    def calc_tempo_viagem(self):
        viagens = self.dados.viagens

        rota_efetiva = self.cria_rota_efetiva()
        
        # Soma o tempo total das viagens da rota efetiva
        tempo_total = 0
        for i in range(len(rota_efetiva)):
            if i == 0:
                continue
            else:
                try:
                    tempo_total += viagens[rota_efetiva[i-1]][rota_efetiva[i]]['tempo']
                    #print(f'{rota_efetiva[i-1]} -> {rota_efetiva[i]}: {viagens[rota_efetiva[i-1]][rota_efetiva[i]]["tempo"]}')
                except KeyError: 
                    raise Exception(f"Viagem entre '{rota_efetiva[i-1]}' e '{rota_efetiva[i]}' não está na lista de viagens.")
        
        return tempo_total
    
    # Retorna o tempo total de roubo da rota
    def calc_tempo_roubo(self):
        tempo_roubo = 0
        sub_rota = self.cria_sub_rota()
        for cidade in sub_rota:
            tempo_roubo += self.dados.itens[cidade]['tempo']
            #print(f"{self.dados.itens[cidade]['item']}: {self.dados.itens[cidade]['tempo']}")
        return tempo_roubo
    
    # Retorna o tempo total da rota
    def calc_tempo_total(self):
        tempo = self.calc_tempo_viagem() + self.calc_tempo_roubo()
        self.tempo_total = tempo
        return tempo

    # Retorna o custo total da rota
    def calc_custo_viagem(self):
        viagens = self.dados.viagens

        rota_efetiva = self.cria_rota_efetiva()

        # Soma o custo total das viagens da rota efetiva
        custo_total = 0
        for i in range(len(rota_efetiva)):
            if i == 0:
                continue
            else:
                try:
                    custo_total += viagens[rota_efetiva[i-1]][rota_efetiva[i]]['custo']
                except KeyError: 
                    raise Exception(f"Viagem entre '{rota_efetiva[i-1]}' e '{rota_efetiva[i]}' não está na lista de viagens.")
        
        return custo_total
    
    # Retorna o lucro total da rota
    def lucro(self):
        return self.valor_total() - self.calc_custo_viagem()


    def fitness(self):

        # Verifica:
        #   - Se a primeira cidade é Escondidos
        #   - Se Escondidos aparece pelo menos duas vezes
        #   - Se Escondidos não é a segunda cidade da rota
        #   - Se a rota efetiva possui cidades repetidas
        if self.rota_valida() == False:
            return float('-inf')
        
        # Verifica se o peso total da rota é maior que 20
        if self.peso_total() > 20:
            self.status = 'Inválida: Peso total maior que 20'
            return float('-inf')
        
        # Verifica se o tempo total da rota é maior que 72
        if self.calc_tempo_total() > 72:
            self.status = 'Inválida: Tempo total maior que 72'
            return float('-inf')
        
        # Retorna o valor total - custo total
        self.status = 'Fit'
        return self.lucro()
