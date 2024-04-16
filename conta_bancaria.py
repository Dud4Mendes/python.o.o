#objeto é uma unica coleçõa de dados(atributos) e comportamentos (métodos) 
class ContaBancaria:
    #atributos são variaveis interns entro do obejeto
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    #métodos são funções que produzem algum compoertamento  
    def depositar(self, valor):
        self.saldo += valor 

    def exibir_detalhes(self):
        print("numero da conta:", self.numero)
        print("titular:", self.titular)
        print("saldo:", self.saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else: 
            print("vc é pobre")   

def exibir_menu():
    print("/nMENU:")
    print("1- exibir detalhes da conta")
    print("2- realiar deposito")
    print("3- realizar saque")
    print("0- sair do programa")         


#aqui stou criando uma instncia do objeto ContaBncaria               
#com o nome conta_do_raphfaelo 
numero_conta = input("digite o numero da conta")
titular_conta = input("digite o titular da conta")
saldo_inicial = float(input("digite o saldo inicual da conta").replace(",","."))               
conta_do_usuario = ContaBancaria(numero_conta, titular_conta, saldo_inicial)

opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("ddigite o numero da opção desejado:"))

    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("digite o valor a ser depositado").replace(",","."))
        conta_do_usuario.depositar(valor_deposito)
    elif opcao == 3:        
        valor_saque = float(input("digite o valor a serr sacado").replace(",","."))
        conta_do_usuario.sacar(valor_saque)



