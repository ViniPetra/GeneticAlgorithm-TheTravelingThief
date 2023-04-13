import rota, rotas
import fabrica_dados as fd

pop = rotas.Rotas(fd.FabricaDados())

pop2 = pop.crossover()

print(len(pop2))