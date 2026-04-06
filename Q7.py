#Nome: Kauãn Felipe da Silva Melo
#Matrícula: 01892125
#--------------------------------------
#Uma estação meteorológica registra temperaturas ao longo do dia. Crie um programa que: 
#• Receba temperaturas até que seja digitado um valor inválido (ex: 999 para encerrar).  
#• Ao final, informe:  
#o Quantas temperaturas foram registradas  
#o Média das temperaturas  
#o Quantas estão acima de 30°C  
#o Quantas estão abaixo de 15°C

contador = 0
soma = 0
acima30 = 0
abaixo15 = 0

while True:
    temp = float(input("Digite a temperatura (ou 999 para encerrar): "))
    
    if temp == 999:
        break
    
    contador += 1
    soma += temp

    if temp > 30:
        acima30 += 1

    if temp < 15:
        abaixo15 += 1

if contador > 0:
    media = soma / contador
else:
    media = 0

print("Quantidade de temperaturas registradas2: ", contador)
print("Média das temperaturas: ", media)
print("Temperaturas acima de 30°C: ", acima30)
print("Temperaturas abaixo de 15°C: ", abaixo15)