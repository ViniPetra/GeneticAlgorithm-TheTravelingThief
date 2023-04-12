GERACOES_MAX = 100000
ERRO_MIN = 0.1

class Populacao:
  def __init__(self,populacao):
    self.tamanho = 10
    self.populacao = populacao
    self.fitness = 0

  def fitness(self, individuo):
    raise NotImplementedError("Implementar")

  def mutacao(self):
    raise NotImplementedError("Implementar")

  def crossover(self):
    raise NotImplementedError("Implementar")

  def selecionar(self, populacao1, populacao2):
    self.populacao = self.populacao + populacao1 + populacao2
    #print(self.populacao)
    #nova_lista = sorted(self.populacao, key=self.fitness, reverse=True)
    
    lista_fit = []
    for item in self.populacao:
      lista_fit.append(item.fitness())
    nova_lista = sorted(lista_fit)

    lista_final = []
    for item in self.populacao:
      for fit in range(10):
        if item.fitness() == nova_lista[fit]:
          lista_final.append(item)
      
        
    self.populacao = lista_final

  def gerar_populacao(self):
    self.populacao = []

    for i in range(self.tamanho):
      self.populacao.append(Individuo())

  def top_fitness(self):
    return self.populacao[0].fitness()

  def top_individuo(self):
    return self.populacao[0]


class Individuo:
  def fitness(self):
    raise NotImplementedError("Implementar")

  def mutacao(self):
    raise NotImplementedError("Implementar")

  def crossover(self):
    raise NotImplementedError("Implementar")

class AlgoritmoGeneticoIndividuo:
  def __init__(self, individuo, geracoes_max=GERACOES_MAX, erro_min=ERRO_MIN):
    self.individuo = individuo
    self.geracoes_max = geracoes_max
    self.erro_min = erro_min
    self.erro = float('inf')
    self.geracoes = 1

  def erro_final(self):
    return self.erro

  def qtd_geracoes(self):
    return self.geracoes
    
  def rodar(self):
    ultimo_fitness = self.individuo.fitness() 

    while True:
      if self.geracoes <= self.geracoes_max and self.erro > self.erro_min:
        novo_individuo = self.individuo.mutacao()
        fitness = novo_individuo.fitness()
        if fitness < ultimo_fitness:
          self.erro = abs(fitness - ultimo_fitness)
          ultimo_fitness = fitness
          self.individuo = novo_individuo
        
        self.geracoes += 1
        if self.geracoes % 5000 == 0: print(f"Geração: {self.geracoes}, Erro: {self.erro}")
      else:
        break
    return self.individuo


class AlgoritmoGeneticoPopulacao:

  def __init__(self, populacao, geracoes_max=GERACOES_MAX, erro_min=ERRO_MIN):
    self.populacao = populacao
    self.geracoes_max = geracoes_max
    self.erro_min = erro_min
    self.erro = float('inf')
    self.geracoes = 1

  def erro_final(self):
    return self.erro

  def qtd_geracoes(self):
    return self.geracoes

  def rodar(self):
    ultimo_fitness = self.populacao.top_fitness()

    while True:
      if self.geracoes <= self.geracoes_max and self.erro > self.erro_min:
        populacao_mutada = self.populacao.mutacao()
        #populacao_crossover = self.populacao.crossover()
        #self.populacao.selecionar(populacao_mutada, populacao_crossover)
        self.populacao.selecionar(populacao_mutada, [])
        fitness = self.populacao.top_fitness()

        if fitness < ultimo_fitness:
          self.erro = abs(fitness - ultimo_fitness)
          ultimo_fitness = fitness
        self.geracoes += 1
        if self.geracoes % 5000 == 0:
          print(f"Geração: {self.geracoes}, Erro: {self.erro}")
      else:
        break
    return self.populacao.top_individuo()
