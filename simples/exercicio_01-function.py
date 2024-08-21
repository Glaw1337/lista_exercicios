# Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área (Pi * (raio * raio))

#Entrada
raio = int(input('Qual o raio? '))       #Variavel


#Processamento
#area = PI * (raio * raio)
def calculoArea(valorRaio):
    PI = 3.14 #constante
    return PI * (valorRaio * valorRaio)



#Saida

print(f"Area do circulo é {calculoArea(raio)}")
# print('A area do circulo é:',area)
#print('A area do circulo é: '+ str(area))

#Lista simples tem o intuito de usar o raciocínio lógico