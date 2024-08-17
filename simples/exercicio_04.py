''' Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um
 determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts),
 as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é
 de 18 watts por metro quadrado.'''


#Entrada
potencia_lampada = float(input('Qual a potência da lâmpada em watts? '))
largura = float(input('Qual a largura do cômodo? '))
comprimento = float(input('Qual o comprimento do cômodo? '))
#Processamento
def calcular_numero_de_lampadas(potencia_lampada, largura, comprimento):
 area = comprimento * largura
 potencia_necessaria = 18 * area
 numero_lampadas = potencia_necessaria / potencia_lampada
 print(f'Serão necessárias {numero_lampadas} lâmpadas')

#Saida
calcular_numero_de_lampadas(potencia_lampada, largura, comprimento)