import csv

class FabricaDados:
    def __init__(self):
        self.viagens = self.gerar_dic_viagens()
        self.cidades = self.gerar_lista_cidades()
        self.itens = self.gerar_dic_items()

    def gerar_dic_viagens(self):
        viagens = {}
        with open('cidades.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            #next(reader)
            for row in reader:
                cidade_origem, cidade_destino, tempo, custo = row
                tempo = float(tempo)
                custo = float(custo)

                #Caminho normal
                if cidade_origem not in viagens:
                    viagens[cidade_origem] = {}
                viagens[cidade_origem][cidade_destino] = {'tempo': tempo, 'custo': custo}
                #Caminho inverso
                if cidade_destino not in viagens:
                    viagens[cidade_destino] = {}
                viagens[cidade_destino][cidade_origem] = {'tempo': tempo, 'custo': custo}
        
        return viagens

    def gerar_lista_cidades(self):
        cidades = []
        with open('cidades.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            #next(reader)
            for row in reader:
                cidade_origem, cidade_destino, dist, valor = row
                if cidade_origem not in cidades:
                    cidades.append(cidade_origem)
        return cidades

    def gerar_dic_items(self):
        items = {}
        with open('items.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            #next(reader)
            for row in reader:
                item, peso, tempo, valor, cidade = row
                peso = int(peso)
                tempo = int(tempo)
                valor = int(valor)
                items[cidade] = {'item': item, 
                                 'peso': peso, 
                                 'tempo': tempo,
                                 'valor': valor}
        return items
    
# fab = FabricaDados()

# for cidade in fab.cidades:
#     print(len(fab.viagens[cidade]))


# print(f"itens: {fab.itens}")
# print("")
# print(f"cidades: {fab.cidades}")
# print("")
# print(f"viagens: {fab.viagens}")

# print(len(fab.itens))
# print(len(fab.cidades))
# print(len(fab.viagens))
