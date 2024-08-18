'''Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do
 combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do
 dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)
 recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.'''

#Entrada 
odometro_inicio = float(input('Digite a marcação do odometro no início do dia: '))
odometro_final = float(input('Digite a marcação do odometro no fim do dia: '))
combustivel_gasto = float(input('Quantos litros de combustível foi gasto? '))
valor_total = float(input('Quanto de dinheiro foi recebido dos passageiros? '))
valor_combustivel_fixo = 4.87

#Processamento
def calculo_media_consumo(odometro_inicio, odometro_final, combustivel_gasto):
    distancia_pecorrida = odometro_final - odometro_inicio
    media_combustivel = distancia_pecorrida / combustivel_gasto
    return media_combustivel
    
def calculo_lucro_liquido_dia(combustivel_gasto, valor_combustivel_fixo, valor_total):
    custo_combustivel_total = combustivel_gasto * valor_combustivel_fixo
    lucro_liquido = valor_total - custo_combustivel_total
    return lucro_liquido

consumo = calculo_media_consumo(odometro_inicio, odometro_final, combustivel_gasto)
lucro = calculo_lucro_liquido_dia(combustivel_gasto, valor_combustivel_fixo, valor_total)
#Saída
print(f'A média de consumo de combustível foi de {consumo}Km/L e o lucro liquido do dia foi R${lucro}.')

