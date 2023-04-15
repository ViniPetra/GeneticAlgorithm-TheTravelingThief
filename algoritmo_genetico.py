GERACOES_MAX = 100000

class AlgoritmoGeneticoPopulacao:

  def __init__(self, populacao, geracoes_max=GERACOES_MAX):
    self.populacao = populacao
    self.geracoes_max = geracoes_max
    self.geracoes = 1

  def qtd_geracoes(self):
    return self.geracoes

  def executar(self):
    ultimo_fitness = self.populacao.top().fitness_val

    while True:
      if self.geracoes <= self.geracoes_max:
        populacao_mutada = self.populacao.mutacao()
        populacao_crossover = self.populacao.crossover()
        self.populacao.selecionar(populacao_mutada, populacao_crossover)
        fitness = self.populacao.top().fitness_val
        if fitness > ultimo_fitness:
          ultimo_fitness = fitness
        self.geracoes += 1
        if self.geracoes % 5000 == 0:
          print(f"Geração: {self.geracoes}, Top fitness: {self.populacao.top().fitness_val}")
      else:
        break
    return self.populacao.top()
