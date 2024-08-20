''' Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
 diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).'''
from datetime import date

#Entrada
ano_nasc = int(input("Qual o seu ano de nascimento? ")) 
#ano_atual = date.today().year

#Processamento

def verificarOpcaoVoto(idadeUser):
    #resposta = ""
    #ano_atual = date.today().year
    #idade = ano_atual - ano_nasc
    if (idadeUser > 16):
        #resposta = "poderá votar"
        return "poderá votar"
    elif(idadeUser > 75):
        #resposta = "não precisará"
        return "não precisará"
    else:
        #resposta = "não poderá votar"    
        return "não poderá votar"

def idade(nascimento):
    ano_atual = date.today().year
    return ano_atual - nascimento                #evitar chamar uma função dentro da outra, pois se uma quebra a outra também quebra.

idadeAtualUser = idade(ano_nasc)

#Saída
print(f"Você tem {idadeAtualUser} anos e segundo a legislação vigente você {verificarOpcaoVoto(idadeAtualUser)} votar esse ano")


#Separar a variável "idade" do código if dará a opção de utilizá-la em outro lugar.