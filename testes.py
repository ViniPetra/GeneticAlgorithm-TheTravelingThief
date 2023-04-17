import rota, rotas, algoritmo_genetico, fabrica_dados as fd
f = fd.FabricaDados()


#-------------------  TESTES  --------------------
#Fábria de dados  
    # Cidades - ok
    # Itens - ok
    # Viagens- ok

# Geração de 1 indivíduo
    # Aleatório
    # Preset
    # Fitness automático na geração de ambos
    # Geração de rotas
    # Mutação

# Geração de uma população
    # Mutação
    # Top
    # Selecionar o melhor
    # Crossover

# Fluxo do Algoritmo Genético
    #selfs
    # if fitness > ultimo_fitness:
    # break

# #Verificar a Fábrica de Dados
# print(f.cidades)
# print("")
# print(f.itens)
# print("")
# print(f.viagens)

# print("")
# print(f"As cidades são únicas? {len(f.cidades) == len(set(f.cidades))}")

# #Teste de geração de indivíduo
# print("")
# ind_rand = rota.Rota(f)
# print("Individuo aleatório:")
# print(ind_rand)
# print("")


# # Teste de gerar individuos aleatórios até que o peso seja maior que 20 ou o tempo maior que 72
# print("Gerando individuos aleatórios até que o peso seja maior que 20 ou o tempo maior que 72...")
# count = 0
# while True:
#     print(f"tentativa: {count}")
#     count += 1
#     ind_rand = rota.Rota(f)
#     if ind_rand.peso > 20 or ind_rand.tempo_total > 72:
#         if ind_rand.fitness_val > float('-inf'):
#             print("Indivíduo inválido gerado:")
#             print (ind_rand)

#             print(" ")
#             print("Testando criar um indivíduo com a rota do indivíduo inválido:")
#             ind_preset = rota.Rota(f, ind_rand.rota)
#             print(ind_preset)
#             print("")
#             print("Testando re-fitnessear o indivíduo inválido:")
#             ind_preset.fitness = ind_preset.fitness()
#             print(ind_preset)
#             break


# ind_teste = rota.Rota(f, rota =['Escondidos', 'Algas', 'Leão', 'Campos', 'Riacho de Fevereiro', 'Leão', 'Além-do-Mar', 'Campos', 'Guardião', 'Santa Paula', 'Riacho de Fevereiro', 'Algas', 'Escondidos', 'Além-do-Mar'])

# print(ind_teste)

# pop = rotas.Rotas(f)

# mutados = pop.mutacao()

# for i in range(len(mutados)):
#     print(f"Mutado {i+1}:")
#     print(mutados[i])
#     print("")


# rota_teste = ['Escondidos', 'Foz da Água Quente', 'Leão', 'Campos', 'Guardião', 'Riacho de Fevereiro', 'Escondidos', 'Campos', 'Ponte-do-Sol', 'Santa Paula', 'Santa Paula', 'Granada', 'Riacho de Fevereiro']
# ind_teste = rota.Rota(f, rota = rota_teste)

# print(f"Rota válida: {ind_teste.rota_valida()}")
# print(f"Valor total: {ind_teste.valor_total()}")
# print(f"Peso total: {ind_teste.peso_total()}")
# print(f"Tempo viagem: {ind_teste.calc_tempo_viagem()}")
# print(f"Tempo roubo: {ind_teste.calc_tempo_roubo()}")
# print(f"Tempo total: {ind_teste.calc_tempo_total()}")
# print(f"Custo total: {ind_teste.calc_custo_viagem()}")
# print(f"Lucro total: {ind_teste.lucro()}")

# pop = rotas.Rotas(f)

# for ind in pop.populacao:
#     print(ind.fitness())
#     print("")

# print(ind_teste.fitness_val)

# temp_arr = []
# i = 1
# while rota_teste[i] != 'Escondidos':
#     temp_arr.append(rota_teste[i])
#     i += 1

# if len(rota_teste) == len(set(rota_teste)):
#     print("Todas as cidades são únicas")


# if(len(temp_arr) == 0):
#     print("Não há cidades na rota")
# else:
#     print(len(temp_arr) == len(set(temp_arr)))

# pop = rotas.Rotas(f)

# # pop_mutada = pop.mutacao()

# pop_cross = pop.crossover()

# # pop_selecionada = pop.selecionar(pop_mutada, pop_cross)

# for ind in pop_cross:
#     print(ind)
#     print("")


#Cruza duas listas de cidades de forma que o padrão seja o seguinte:
#1. primeira cidade da primeira lista
#2. segunda cidade da segunda lista
#3. terceira cidade da primeira lista
#4. quarta cidade da segunda lista

# def cruzar(lista1, lista2):
    
#     nova_lista1 = []
#     nova_lista2 = []

#     for i in range(len(lista1)):
#         if i % 2 == 0:
#             nova_lista1.append(lista1[i])
#             nova_lista2.append(lista2[i])
#         else:
#             nova_lista1.append(lista2[i])
#             nova_lista2.append(lista1[i])

#     return nova_lista1, nova_lista2


# listaa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# listab = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

# print(cruzar(listaa, listab))


# pop = rotas.Rotas(f)

# pop_mutada = pop.mutacao()

# pop_cross = pop.crossover()

# pop.selecionar(pop_mutada, pop_cross)


# # for ind in pop_selecionada:
# #     print(ind)
# #     print("")

# print(type(pop.populacao))
# print(type(pop_selecionada))

# alg_gen = algoritmo_genetico.AlgoritmoGeneticoPopulacao(rotas.Rotas(fd.FabricaDados()))

# individuo_adaptado = alg_gen.executar()

# ind_teste = rota.Rota(fd.FabricaDados(), rota = individuo_adaptado.rota)

# print('-----------------')
# print(ind_teste)

# presets = [
#     ['Escondidos', 'Algas', 'Leão', 'Campos', 'Riacho de Fevereiro', 'Leão', 'Além-do-Mar', 'Campos', 'Guardião', 'Santa Paula', 'Riacho de Fevereiro', 'Algas', 'Escondidos', 'Além-do-Mar'],
#     ['Escondidos', 'Foz da Água Quente', 'Leão', 'Campos', 'Guardião', 'Riacho de Fevereiro', 'Escondidos', 'Campos', 'Ponte-do-Sol', 'Santa Paula', 'Santa Paula', 'Granada', 'Riacho de Fevereiro'],
#     ['Escondidos', 'Algas', 'Leão', 'Campos', 'Riacho de Fevereiro', 'Leão', 'Além-do-Mar', 'Campos', 'Guardião', 'Santa Paula', 'Riacho de Fevereiro', 'Algas', 'Escondidos', 'Além-do-Mar'],
#     ['Escondidos', 'Foz da Água Quente', 'Leão', 'Campos', 'Guardião', 'Riacho de Fevereiro', 'Escondidos', 'Campos', 'Ponte-do-Sol', 'Santa Paula', 'Santa Paula', 'Granada', 'Riacho de Fevereiro'],
#     ['Escondidos', 'Algas', 'Leão', 'Campos', 'Riacho de Fevereiro', 'Leão', 'Além-do-Mar', 'Campos', 'Guardião', 'Santa Paula', 'Riacho de Fevereiro', 'Algas', 'Escondidos', 'Além-do-Mar'],
# ]

# pop = rotas.Rotas(fd.FabricaDados(), presets)

# for ind in pop.populacao:
#     print(ind)
#     print("")

# pop = rotas.Rotas(fd.FabricaDados())

# for ind in pop.populacao:
#     print(ind)
#     print("")

# r = ['Escondidos', 'Leão', 'Além-do-Mar', 'Escondidos', 'Escondidos', 'Campos', 'Foz da Água Quente', 'Granada', 'Guardião', 'Riacho de Fevereiro', 'Riacho de Fevereiro', 'Porto', 'Guardião', 'Santa Paula']

# ind_teste = rota.Rota(fd.FabricaDados(), rota = r)

# print(ind_teste)

r = ['Escondidos', 'Lagos', 'Santa Paula', 'Além-do-Mar', 'Escondidos', 'Algas', 'Porto', 'Santa Paula', 'Granada', 'Ponte-do-Sol', 'Ponte-do-Sol', 'Leão', 'Riacho de Fevereiro', 'Campos']
ind_teste = rota.Rota(fd.FabricaDados(), rota = r)
print(ind_teste)

#fit 36707
#peso 20
#tempo 67

# while True:
#     pop = rotas.Rotas(fd.FabricaDados())
#     pop_m = pop.mutacao()
#     pop_c = pop.crossover()
#     pop.selecionar(pop_m, pop_c)

#     for ind in pop.populacao:
#         if ind.fitness_val > float("-inf"):
#             novo_fit = ind.fitness()
#             if novo_fit != ind.fitness_val:
#                 print("Erro")
                