from algoritmo_genetico import Populacao
import rota

class Rotas(Populacao):
  def __init__(self, dados):
    self.tamanho = 10
    self.fitness = 0
    self.populacao = []

    for i in range(self.tamanho):
      self.populacao.append(rota.Rota(dados))


  def crossover(self):
    nova_população = []
    
    meio = len(self.populacao)// 2
    
    print(f"meio: {meio}")
    
    metade1 = self.populacao[:meio]
    metade2 = self.populacao[meio:]
    
    for i in range(meio):
      metade_da_rota1 = metade1[i].rota[:len(metade1[i].rota)//2]
      metade_da_rota2 = metade2[i].rota[len(metade2[i].rota)//2:]
      
      metade_da_rota3 = metade1[i].rota[len(metade1[i].rota)//2:]
      metade_da_rota4 = metade2[i].rota[:len(metade2[i].rota)//2]
      
      frankenstein1 = metade_da_rota1 + metade_da_rota2
      frankenstein2 = metade_da_rota3 + metade_da_rota4

      nova_população.append(frankenstein1)
      nova_população.append(frankenstein2)

    return self.populacao + nova_população
    
  #Testar
  def mutacao(self):
    for item in self.populacao:
      item.mutacao()
      
  # def __str__(self):
  #   print(" ")
  #   print(f"Objeto Rotas:")
  #   print(f"Tamanho da população: {self.tamanho}")
  #   print(" ")
  #   print("Itens da população:")
  #   for item in self.populacao:
  #     print(item.__str__())
  #   print(" ")
  #   return ""
    
    
#pop.crossover()


#   def fitness(self, individuo):
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
