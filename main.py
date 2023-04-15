import rotas, algoritmo_genetico, rota
import fabrica_dados as fd

alg_gen = algoritmo_genetico.AlgoritmoGeneticoPopulacao(rotas.Rotas(fd.FabricaDados()))

individuo_adaptado = alg_gen.executar()

print("\nPrimeiro mais adaptado:")
print(f"Quantidade de gerações: {alg_gen.qtd_geracoes()}")
print(individuo_adaptado)

#--------------------  TESTES  --------------------
#roda o algoritmo genetico 10x e gurda todos os melhores individuos 
# melhores = []
# for i in range(5):
#     print(f"Rodada: {i+1}")
#     ag = algoritmo_genetico.AlgoritmoGeneticoPopulacao(rotas.Rotas(fd.FabricaDados()))
#     melhores.append(ag.executar())
#     print("")

# #imprime os melhores individuos
# for i in range(len(melhores)):
#     print(f"Melhor individuo {i+1}:")
#     print(f"fitness: {melhores[i].fitness_val}")
#     print(f"rota: {melhores[i].rota}")
#     print(f"peso: {melhores[i].peso}")
#     print(f"tempo: {melhores[i].tempo_total}")
#     print("")

#TESTE DE GERAÇÃO DE INDIVIDUOS

# ind_rand = rota.Rota(fd.FabricaDados())

#rota_preset = ['Escondidos', 'Porto', 'Leão', 'Granada', 'Campos', 'Riacho de Fevereiro', 'Além-do-Mar', 'Escondidos', 'Santa Paula', 'Algas', 'Guardião', 'Foz da Água Quente', 'Lagos', 'Ponte-do-Sol']
#ind_preset = rota.Rota(fd.FabricaDados(), rota_preset)

#fit = 214137
#peso = 15
#tempo = 65

# print("")