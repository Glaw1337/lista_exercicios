''' Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor
 correspondente em graus Fahrenheit. (F = (C * 9/5) + 32)'''

#Entrada
Cel = int(input('Insira a temperatura em graus Celsius: '))

#Processamento
F = (Cel * 9/5) + 32

#Saida
print('Sua temperatura em Fahrenheit é: ' , F)
