'''A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de
 seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
 reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de
 voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de
 combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para
 percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os
 abastecimentos é o mesmo.'''


#entrada
comprimento = float(input('Qual o comprimento da pista(em metros)? '))  #Não sabe o valor que o usuário irá colocar, usa Float ao inves de Int.
voltas = int(input('Qual o numero total de voltas? '))
abastecimento = int(input('Numero de abastecimentos desejados: '))
consumo = float(input('Consumo de combustivel do carro (em Km/L)? '))

#processamento
kmTotal = (comprimento/1000) * voltas  #Escrever codigo de forma separada é melhor para a manuntenção do mesmo
consumoTotal = kmTotal/consumo
litros = consumoTotal / abastecimento

#saida
print('O número mínimo de litros necessários até o primeiro reabastecimento: ', litros)


#Sempre bom quando for realizar a execução de uma tarefa na programação, separar ela por 3 etapas(que seriam as de cima) para melhor resolução da tarefa.
#