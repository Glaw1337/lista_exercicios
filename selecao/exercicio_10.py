'''Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
 escrevê-los em ordem crescente.'''
#        exercicio importante, refazer sempre que possivel 
#        (CTRL + ;) adiciona comentario

valor1 = int(input("Insira o primeiro número: "))
valor2 = int(input("Insira o segundo número: "))
valor3 = int(input("Insira o terceiro número: "))
reposta = ""
if( valor1 < valor2 and valor2 < valor3 ):
    resposta= valor1, valor2 , valor3 
elif( valor1 < valor3 and valor3 < valor2 ): 
    resposta = valor1, valor3, valor2
elif( valor2 < valor3 and valor3 < valor1 ): 
    resposta = valor2, valor3, valor1
elif( valor2 < valor1 and valor1 < valor3 ): 
    resposta = valor2, valor1, valor3
elif( valor3 < valor1 and valor1 < valor2 ): 
    resposta = valor3, valor1, valor2
else:#  valor3 < valor2 and valor2 < valor3 
    resposta = valor3, valor2, valor3

print(resposta)    

