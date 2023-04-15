import rotas, algoritmo_genetico
import fabrica_dados as fd

alg_gen = algoritmo_genetico.AlgoritmoGeneticoPopulacao(rotas.Rotas(fd.FabricaDados()))

individuo_adaptado = alg_gen.executar()

print("\nPrimeiro mais adaptado:")
print(f"Quantidade de gerações: {alg_gen.qtd_geracoes()}")
print(individuo_adaptado)
