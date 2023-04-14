import rotas, algoritmo_genetico, rota
import fabrica_dados as fd
import requests, json

alg_gen = algoritmo_genetico.AlgoritmoGeneticoPopulacao(rotas.Rotas(fd.FabricaDados()))

individuo_adaptado = alg_gen.executar()

print("\nPrimeiro mais adaptado:")
print(f"Quantidade de gerações: {alg_gen.qtd_geracoes()}")
print(f"Erro: {alg_gen.erro_final()}")
print(individuo_adaptado)

#--------------------  TESTES  --------------------
# rota_teste = ['Escondidos', 'Algas', 'Riacho de Fevereiro', 'Guardião', 'Lagos', 'Santa Paula', 'Foz da Água Quente', 'Porto', 'Campos', 'Além-do-Mar', 'Granada', 'Escondidos', 'Leão', 'Ponte-do-Sol']

# ind = rota.Rota(dados=fd.FabricaDados())
# ind2 = rota.Rota(dados=fd.FabricaDados(), rota=rota_teste)

# print("")
# print("Indivíduos:")
# print(ind)
# print(ind2)
# print("")
# print("Tipos:")
# print(type(ind))
# print(type(ind2))
# print("")
# print("Fitness:")
# print(ind.fitness_val)
# print(ind2.fitness_val)
# print("")
# print("Mutação:")
# print(ind.mutacao())
# print(ind2.mutacao())

# rota_teste2 = ['Algas', 'Escondidos', 'Riacho de Fevereiro', 'Guardião', 'Lagos', 'Santa Paula', 'Foz da Água Quente', 'Porto', 'Campos', 'Além-do-Mar', 'Granada', 'Escondidos', 'Leão', 'Ponte-do-Sol']
# ind = rota.Rota(dados=fd.FabricaDados(), rota=rota_teste2)

# print(ind.fitness_val)

# ind1 = rotas.Rotas(dados=fd.FabricaDados())
# ind2 = rotas.Rotas(dados=fd.FabricaDados())
# mut = ind1.mutacao()
# mut2 = ind2.mutacao()

# ind1.selecionar(mut, mut2)

# rota_invalida = ['Lagos', 'Ponte-do-Sol', 'Campos', 'Escondidos', 'Porto', 'Leão', 'Santa Paula', 'Riacho de Fevereiro', 'Granada', 'Escondidos', 'Algas', 'Além-do-Mar', 'Foz da Água Quente', 'Guardião']

# ind_inv = rota.Rota(dados=fd.FabricaDados(), rota=rota_invalida)

# print(ind_inv.fitness_val)

# while True:
#     ind = rota.Rota(dados=fd.FabricaDados())
#     ind = ind.mutacao()
#     print(f"fitness: {ind.fitness_val}, rota[0]: {ind.rota[0]}")
#     if ind.fitness_val != float('-inf') and ind.rota[0] != 'Escondidos':
#         break


# while True:
#     populacao = rotas.Rotas(dados=fd.FabricaDados())
#     pop = populacao.crossover()
#     for ind in pop:     
#         print(f"fitness: {ind.fitness_val}, rota[0]: {ind.rota[0]}")
#         if ind.fitness_val != float('-inf') and ind.rota[0] != 'Escondidos':
#             print("Deu merda")
#             break

# while True:
#     populacao = rotas.Rotas(dados=fd.FabricaDados())
#     populacao2 = rotas.Rotas(dados=fd.FabricaDados())
#     populacao3 = rotas.Rotas(dados=fd.FabricaDados())
    
#     populacao.selecionar(populacao2.populacao, populacao3.populacao)
    
#     pop = populacao.populacao
#     for ind in pop:     
#         print(f"fitness: {ind.fitness_val}, rota[0]: {ind.rota[0]}")
#         if ind.fitness_val != float('-inf') and ind.rota[0] != 'Escondidos':
#             print("Deu merda")
#             break

# rota_teste = ['Escondidos', 'Ponte-do-Sol', 'Porto', 'Granada', 'Escondidos', 'Campos', 'Lagos', 'Santa Paula', 'Algas', 'Ponte-do-Sol', 'Lagos', 'Leão', 'Granada', 'Riacho de Fevereiro']

# ind = rota.Rota(dados=fd.FabricaDados())

# print("")

#TESTAR SE O CROSSOVER CHAMA O FITNESS

# pop = rotas.Rotas(dados=fd.FabricaDados())

# pop_cross, teste_fit = pop.crossover()

# newpop = []
# for item in teste_fit:
#     newpop.append(rota.Rota(dados=fd.FabricaDados(), rota=item))


# for i in range(len(newpop)):
#     if(pop_cross[i].fitness_val != newpop[i].fitness_val):
#         print(f"fitness: {pop_cross[i].fitness_val}, rota: {pop_cross[i].rota}")
#         print(f"fitness: {newpop[i].fitness_val}, rota: {newpop[i].rota}")
#         print("")
#     else:
#         print("Valores iguais")

# teste = ['Escondidos', 'Algas', 'Porto', 'Riacho de Fevereiro', 'Santa Paula', 'Santa Paula', 'Além-do-Mar', 'Escondidos', 'Lagos', 'Campos', 'Leão', 'Santa Paula', 'Campos', 'Riacho de Fevereiro']

# if teste[0] != "Escondidos":
#     print(float('-inf'))

# if teste.count('Escondidos') != 2:
#     print(float('-inf'))

# temp_arr = []
# i = 1
# while teste[i] != 'Escondidos':
#     temp_arr.append(teste[i])
#     i += 1

# if len(temp_arr) != len(set(temp_arr)):
#     print(float('-inf'))

# ind = rota.Rota(dados=fd.FabricaDados())

# print("--------------------")
# print(f"fitness: {ind.fitness_val}")
# print(f"rota: {ind.rota}")
# print(f"peso: {ind.peso}")
# print(f"tempo: {ind.tempo_total}")
# print("--------------------")

#gera novos indivíduos até que um tenha fitness válido mas peso > 20 e tempo >72
# while True:
#     ind = rota.Rota(dados=fd.FabricaDados())
#     print("--------------------")
#     print(f"fitness: {ind.fitness_val}")
#     print(f"rota: {ind.rota}")
#     print(f"peso: {ind.peso}")
#     print(f"tempo: {ind.tempo_total}")
#     print("--------------------")

#     if ind.fitness_val != float('-inf') and ind.peso > 20 and ind.tempo_total > 72:
#         print("Deu merda")
#         break