class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_informacoes(self):
        print("marca: ", self.marca)  
        print("modelo: ", self.modelo)
        print("cor: ", self.cor) 
        print("ano: ", self.ano) 


carro1 = Carro("toyota", "corolla", "prata", 2002)
carro2 = Carro("honda", "civic", "preto", 2023)        

carro1.exibir_informacoes()
carro2.exibir_informacoes()

input()