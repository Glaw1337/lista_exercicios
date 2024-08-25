'''As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
 compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e
 escreva o valor total da compra.'''

macas = int(input("Quantidade maçãs compradas: "))
def CalculoMacas(QtdMacas):
    if QtdMacas < 12:
        ValorTotal = QtdMacas * 0.30
        return ValorTotal
    else:
        ValorTotal = QtdMacas * 0.25
        return ValorTotal
                            #ValorMacas = CalculoMacas(macas)
print(f"O valor total foi de R${CalculoMacas(macas)}")    #print(f"O valor total foi de R${ValorMacas}")    

