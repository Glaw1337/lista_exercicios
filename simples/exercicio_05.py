'''Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e
 altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas
 paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de
 azulejos possui 1,5 m2'''

#Entrada
comprimento = float(input('Qual o comprimento da sua cozinha? '))
largura = float(input('Qual a largura da sua cozinha? '))
altura = float(input('Qual a altura da sua cozinha? '))
#Processamento
def calcular_quantidade_de_caixas(comprimento, largura, altura):
    area1 = comprimento * largura
    area2 = largura * altura
    area_total = 2 * (area1 + area2)
    cobertura_azulejo = 1.5
    caixas_azulejo = area_total / cobertura_azulejo
    return caixas_azulejo

caixas_necessarias = calcular_quantidade_de_caixas(comprimento, largura, altura)

#Saida
print(f'Será necessário {caixas_necessarias} caixas de azulejos para cobrir todas as paredes.')