import rota

class Rotas():
  #Cria uma população de rotas
  def __init__(self, dados):
    self.tamanho = 10
    self.populacao = []
    self.dados = dados

    for i in range(self.tamanho):
      self.populacao.append(rota.Rota(dados))

  #retorna uma lista com os individuos cruzados da população
  def crossover(self):
    nova_população = []
    
    meio = len(self.populacao)// 2
    
    metade1 = self.populacao[:meio]
    metade2 = self.populacao[meio:]
    
    for i in range(meio):
      metade_da_rota1 = metade1[i].rota[:len(metade1[i].rota)//2]
      metade_da_rota2 = metade2[i].rota[len(metade2[i].rota)//2:]
      
      metade_da_rota3 = metade1[i].rota[len(metade1[i].rota)//2:]
      metade_da_rota4 = metade2[i].rota[:len(metade2[i].rota)//2]
      
      frankenstein1 = metade_da_rota1 + metade_da_rota2
      frankenstein2 = metade_da_rota3 + metade_da_rota4

      nova_população.append(rota.Rota(self.dados, rota=frankenstein1))
      nova_população.append(rota.Rota(self.dados, rota=frankenstein2))

    return nova_população

  #retorna uma lista com os individuos mutados da população
  def mutacao(self):
    mutados = []
    for individuo in self.populacao:
      mutado = individuo.mutacao()
      mutados.append(mutado)
    return mutados
      
  #retorna o fitness do melhor individuo da população e o objeto do individuo
  def top_fitness(self):
    lista_ordenada = sorted(self.populacao, key=lambda x: x.fitness_val, reverse=True)
    return lista_ordenada[0].fitness_val
  
  #seleciona os 10 melhores individuos da população
  def selecionar(self, populacao1, populacao2):
    self.populacao = self.populacao + populacao1 + populacao2
    

    # for item in self.populacao:
    #   if item.fitness_val != float('-inf') and item.rota[0] != 'Escondidos':
    #     print(item.rota)
    #     print(item.fitness_val)
    #     print(" ")
        
    
    lista_ordenada = sorted(self.populacao, key=lambda x: x.fitness_val, reverse=True)
    self.populacao = lista_ordenada[:10]
    
  #retorna uma lista com os fitness de todos os individuos da população
  def ver_fitness(self):
    lista_fit = []
    for item in self.populacao:
      lista_fit.append(item.fitness_val)
    return lista_fit
  
  def top_individuo(self):
    lista_ordenada = sorted(self.populacao, key=lambda x: x.fitness_val, reverse=True)
    return lista_ordenada[0].fitness_val
  

