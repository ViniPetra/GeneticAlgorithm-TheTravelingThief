import rota

class Rotas():
  #Cria uma população de rotas
  def __init__(self, dados):
    self.tamanho = 10
    self.populacao = []
    self.dados = dados

    for i in range(self.tamanho):
      self.populacao.append(rota.Rota(dados))

  # #retorna uma lista com os individuos cruzados da população
  # def crossover(self):
  #   nova_população = []
  #   novas_rotas = []

  #   meio = len(self.populacao)// 2
    
  #   metade1 = self.populacao[:meio]
  #   metade2 = self.populacao[meio:]
    
  #   for i in range(meio):
  #     primeira_cidade = [metade1[i].rota[0]]

  #     metade_da_rota1 = metade1[i].rota[1:len(metade1[i].rota)//2]
  #     metade_da_rota2 = metade2[i].rota[len(metade2[i].rota)//2:]
  #     metade_da_rota3 = metade1[i].rota[len(metade1[i].rota)//2:]
  #     metade_da_rota4 = metade2[i].rota[1:len(metade2[i].rota)//2]
      
  #     frankenstein1 = primeira_cidade + metade_da_rota2 + metade_da_rota1
  #     frankenstein2 = primeira_cidade + metade_da_rota4 + metade_da_rota3

  #     novas_rotas.append(frankenstein1)
  #     novas_rotas.append(frankenstein2)

  #     for rotas in novas_rotas:
  #       nova_população.append(rota.Rota(self.dados, rotas))

  #   return nova_população

  #retorna uma lista com os individuos mutados da população
  def mutacao(self):
    mutados = []
    for individuo in self.populacao:
      mutado = individuo.mutacao()
      mutados.append(mutado)
    return mutados

  #retorna o individuo mais adaptado da população
  def top(self):
    lista_ordenada = sorted(self.populacao, key=lambda x: x.fitness(), reverse=True)
    return lista_ordenada[0]

  #seleciona os 10 melhores individuos da população
  def selecionar(self, populacao1, populacao2):
    populacao_total = self.populacao + populacao1 + populacao2
    lista_ordenada = sorted(populacao_total, key=lambda x: x.fitness(), reverse=True)
    mais_adaptados = lista_ordenada[:10]
    self.populacao = mais_adaptados
    return mais_adaptados

  def cruzar(lista1, lista2):
      
      nova_lista1 = []
      nova_lista2 = []

      for i in range(len(lista1)):
          if i % 2 == 0:
              nova_lista1.append(lista1[i])
              nova_lista2.append(lista2[i])
          else:
              nova_lista1.append(lista2[i])
              nova_lista2.append(lista1[i])

      return nova_lista1, nova_lista2

  
  def crossover(self):
    nova_populacao = []
    novos_individuos = []

    tamanho_pop = len(self.populacao)
    metade = tamanho_pop // 2

    metade_1 = self.populacao[:metade]
    metade_2 = self.populacao[metade:]

    for i in range(metade):
      nova_lista1, nova_lista2 = Rotas.cruzar(metade_1[i].rota, metade_2[i].rota)
      novos_individuos.append(nova_lista1)
      novos_individuos.append(nova_lista2)

    for individuo in novos_individuos:
      nova_populacao.append(rota.Rota(self.dados, individuo))

    return nova_populacao
