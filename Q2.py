#Nome: Kauãn Felipe da Silva Melo
#Matrícula: 01892125
#--------------------------------------
#Fazer  um  algoritmo  que  receba  um  valor  “n”  no  teclado  e  determine  o  maior.  A  condição  de  término  do 
#algoritmo é quando o usuário digitar zero. 

maior = None

while True:
    n = int(input("Digite um número (0 para parar): "))
    
    if n == 0:
        break
    
    if maior is None or n > maior:
        maior = n

if maior is not None:
    print("O maior número digitado foi:", maior)
else:
    print("Nenhum número válido foi digitado.")