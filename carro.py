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

carros = []

while True:
    marca = input("insira a marca do carro ou 'sair'para encerrar o programa: ")

    if marca.lower() == "sair":
        break

    modelo = input("insira o modelo do carro")
    cor = input("insira a cor do carro")
    ano = input("insira o ano do veiculo")

    carro = Carro(marca, modelo, cor, ano)
    carros.append(carro)

print("/n informações dos carros: ")
for i, carro in enumerate(carros, start=1):
    print(f"/n Carro {i}")
    carro.exibir_informacoes()

input()        

