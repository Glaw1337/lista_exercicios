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
    area = comprimento * largura
    

#Saida
