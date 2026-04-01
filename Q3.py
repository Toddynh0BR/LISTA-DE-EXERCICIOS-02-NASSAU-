#Nome: Guilherme Fortaleza de Souza
#Matrícula: 01877047
#--------------------------------------
#Escreva  um  algoritmo  que  solicite  a  idade  de  10  pessoas  e  imprima:  Total  de  pessoas  com  menos  de  21 
#anos. Total de pessoas com mais de 50 anos.

# variaveis

maior_50 = 0
menor_21 = 0

# cadastro da idade e a quantidade
for i in range(10):
    idade = int(input("Digite a idade: "))
    
# o a condinção if e elif armazena os dados da idade
    
    if idade > 50:
        maior_50 += 1
    elif idade < 21:
        menor_21 += 1

# impressão dos resultados dos dados       

print(f"Quantidade de pessoas com mais de 50 anos: {maior_50}")
print(f"Quantidade de pessoas com menos de 21 anos: {menor_21}")
 