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

# print(ind1.ver_fitness())

# mut = ind1.mutacao()
# mut2 = ind2.mutacao()

# print(ind1.ver_fitness())
# print(ind2.ver_fitness())

# ind1.selecionar(mut, mut2)

# print(ind1.ver_fitness())

# print(abs(ind1.ver_fitness()[1] - ind1.ver_fitness()[0]))
