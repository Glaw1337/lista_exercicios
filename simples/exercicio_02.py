#Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
#correspondente em graus Celsius. (C = (F-32) * 5 / 9)

#Entrada 
Fah = float(input('Digite a temperatura: '))

#Processamento
Cel = (Fah-32) * 5/9

#Saida
print('A temperatura em Celsius é: ' , Cel)
