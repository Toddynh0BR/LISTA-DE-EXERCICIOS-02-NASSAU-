#Nome: Áquila Pedro Joaquim Oliveira da Silva
#Matrícula: 01890876
#--------------------------------------
#Escreva um algoritmo que imprima os 100 primeiros números Pares. 

contador = 0 
numero = 1 

while contador < 100:
    if numero % 2 == 0:
        print(numero)
        contador += 1
    numero += 1