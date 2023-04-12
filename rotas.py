from algoritmo_genetico import Populacao
import rota

class Rotas(Populacao):
  def __init__(self):
    self.tamanho = 10
    self.fitness = 0
    self.populacao = []

    for i in range(self.tamanho):
      self.populacao.append(rota.Rota())

#   def fitness(self, individuo):
#     raise NotImplementedError("Implementar")

#   def mutacao(self):
#     raise NotImplementedError("Implementar")

#   def crossover(self):
#     raise NotImplementedError("Implementar")

#   def selecionar(self, populacao1, populacao2):
#     self.populacao = self.populacao + populacao1 + populacao2
#     #print(self.populacao)
#     #nova_lista = sorted(self.populacao, key=self.fitness, reverse=True)
    
#     lista_fit = []
#     for item in self.populacao:
#       lista_fit.append(item.fitness())
#     nova_lista = sorted(lista_fit)

#     lista_final = []
#     for item in self.populacao:
#       for fit in range(10):
#         if item.fitness() == nova_lista[fit]:
#           lista_final.append(item)
      
        
#     self.populacao = lista_final

#   def top_fitness(self):
#     return self.populacao[0].fitness()

#   def top_individuo(self):
#     return self.populacao[0]
