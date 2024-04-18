num1 = int(input("digite um numero"))
num2 = int(input("digite outro numero"))
operacao = input("digite um operçao")

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def divisao(num1, num2):
    if num2 == 0:
        return "o numero nao pode ser dividido por 0"
    else:
        return num1 / num2

def multiplicacao(num1, num2):
    return num1 * num2

if (operacao == '+'):
    print(somar(num1, num2))

elif (operacao == '-'):
    print(subtrair(num1, num2))

elif (operacao == '/'):
    print(divisao(num1, num2))

elif (operacao == '*'):
    print(multiplicacao(num1, num2))

else:
    print("invalido")
