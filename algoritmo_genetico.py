GERACOES_MAX = 100000

class AlgoritmoGeneticoPopulacao:

  def __init__(self, populacao, geracoes_max=GERACOES_MAX):
    self.populacao = populacao
    self.geracoes_max = geracoes_max
    self.geracoes = 1

  def qtd_geracoes(self):
    return self.geracoes

  def executar(self):
    # Define o melhor fitness da primeira geração
    ultimo_fitness = self.populacao.top()

    while True:
      if self.geracoes <= self.geracoes_max:
        populacao_mutada = self.populacao.mutacao() # Mutação
        populacao_crossover = self.populacao.crossover() # Crossover
        self.populacao.selecionar(populacao_mutada, populacao_crossover) 
        fitness = self.populacao.top() # Melhor fitness da geração
        # Se o fitness da geração for melhor que o da última geração
        if fitness.fitness_val > ultimo_fitness.fitness_val:
          ultimo_fitness = fitness # Atualiza o melhor fitness
        self.geracoes += 1 # Incrementa o número de gerações
        if self.geracoes % 10000 == 0: # Imprime o melhor fitness a cada 10000 gerações
          print(f"Geração: {self.geracoes}\nTop fitness: \n{ultimo_fitness}\n\n")
      else:
        break
    
    return ultimo_fitness # Retorna o melhor fitness da última geração
