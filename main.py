import rotas, algoritmo_genetico, rota
import fabrica_dados as fd

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