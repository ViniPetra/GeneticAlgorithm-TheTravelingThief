GERACOES_MAX = 100000
ERRO_MIN = 0.1

class AlgoritmoGeneticoPopulacao:

  def __init__(self, populacao, geracoes_max=GERACOES_MAX, erro_min=ERRO_MIN):
    self.populacao = populacao
    self.geracoes_max = geracoes_max
    self.erro_min = erro_min
    self.erro = float('inf')
    self.geracoes = 1
    print("-Instanciado Algoritmo Genético-")

  def erro_final(self):
    return self.erro

  def qtd_geracoes(self):
    return self.geracoes

  def executar(self):
    ultimo_fitness = self.populacao.top().fitness_val

    while True:
      if self.geracoes <= self.geracoes_max and self.erro > self.erro_min:
        populacao_mutada = self.populacao.mutacao()
        populacao_crossover = self.populacao.crossover()
        self.populacao.selecionar(populacao_mutada, populacao_crossover)
        fitness = self.populacao.top().fitness_val
        if fitness > ultimo_fitness:
          self.erro = abs(fitness - ultimo_fitness)
          ultimo_fitness = fitness
        self.geracoes += 1
        if self.geracoes % 5000 == 0:
          print(f"Geração: {self.geracoes}, Erro: {self.erro}")
      else:
        break
    return self.populacao.top()
