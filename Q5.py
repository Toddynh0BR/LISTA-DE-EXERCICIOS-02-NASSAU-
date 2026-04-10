#Nome: Guilherme Fortaleza de Souza
#Matrícula: 01877047
#--------------------------------------
#Uma escola está realizando uma votação para escolher o representante de turma. 
#Crie um programa que: 
#• Permita a entrada de votos até que o usuário digite 0 para encerrar.  
#• As opções são:  
#o 1 → Candidato A  
#o 2 → Candidato B  
#o 3 → Candidato C  
#• Conte quantos votos cada candidato recebeu.  
#• Ao final, exiba:  
#o Total de votos por candidato  
#o Total de votos válidos  
#o O candidato vencedor  
#Considere votos inválidos (números fora das opções) e não os contabilize. 

# criei uma variavel 'list' pra guardar o nome dos candidados

list = ["Candidato A", "Candidato B", "Candidato C"]

# aqui adicionei mais 3 variaveis para contar os votos de cada candidato

contadorA = 0
contadorB = 0
contadorC = 0

# aqui coloquei o join para separar os candidatos com quebra linha e um for e len para enumerar e mostrar os candidatos para o usuario escolher

print ('\n'.join(f'{i+1}: {list[i]}' for i in range(len(list))))

# coloquei um loop como foi pedido na questão que se quebra quando digita 0

while True:
        
# aqui o usuario digita o numero do candidato
        
        voto = int(input("Digite o número do candidato para votar (0 para encerrar): "))
        
# aqui são condições, o user decide o voto e computador armazena e soma esse voto na varivel ou encerra o loop se digitar 0      
        
        if voto == 0:
            break
        elif voto == 1:
            contadorA += 1
        elif voto == 2:
            contadorB += 1
        elif voto == 3:
            contadorC += 1
 
 # esse else é para caso o user digite um numero invalido, ele mostra a mensagem e volta para o inicio do loop para tentar novamente
 
        else:
            print("Voto inválido. Tente novamente.")
        continue

# aqui o programa mostra o total de votos para cada candidato usando as variaveis que foram somando os votos durante o loop

print(f"Total de votos para {list[0]}: {contadorA}")
print(f"Total de votos para {list[1]}: {contadorB}")
print(f"Total de votos para {list[2]}: {contadorC}")


