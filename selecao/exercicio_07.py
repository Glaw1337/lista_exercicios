'''Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e
 escrever o maior deles.'''

#entrada de dados
valor1 = float(input("Insira um valor: "))
valor2 = float(input("Insira outro valor: "))
#processamento de dados
resposta = 0    #numero mais neutro para definir uma variavel numerica
if valor1 > valor2:
    resposta = valor1
else:
    resposta = valor2 #forma dinamica para poupar tempo no processador da maquina do usuario, ao inves de repetir if valor1 < valor2
 
 #resposta = valor1 if valor1 > valor2 else valor2 // Utilizando Ternario, sempre que possivel utilize o Ternario.
 #                                                    Ternario é  aconselhavel utilizar quando o comando if tive apenas 2 alternativas.             
 #resposta = (valor1 > valor2) ? valor1 : valor2 // javascript

#saida de dados
print("O valor maior é: ", resposta) #print(f"O {resposta} é o valor maior.")
