GERACOES_MAX = 100000

class AlgoritmoGeneticoPopulacao:

  def __init__(self, populacao, geracoes_max=GERACOES_MAX):
    self.populacao = populacao
    self.geracoes_max = geracoes_max
    self.geracoes = 1

  def qtd_geracoes(self):
    return self.geracoes

  def executar(self):
    ultimo_fitness = self.populacao.top()

    while True:
      if self.geracoes <= self.geracoes_max:
        populacao_mutada = self.populacao.mutacao()
        populacao_crossover = self.populacao.crossover()
        self.populacao.selecionar(populacao_mutada, populacao_crossover)
        fitness = self.populacao.top()
        if fitness.fitness() > ultimo_fitness.fitness():
          ultimo_fitness = fitness
        self.geracoes += 1
        if self.geracoes % 10000 == 0:
          print(f"Geração: {self.geracoes}\nTop fitness: \n{ultimo_fitness}\n\n")
      else:
        break
    
    return ultimo_fitness
