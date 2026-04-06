#Nome: Matheus Augusto Gomes da Silva
#Matrícula: 01894714
#--------------------------------------
#Uma empresa deseja analisar o perfil de seus clientes. Crie um programa que: 
#• Permita cadastrar 20  clientes, informando:  
#• Idade  
#• Sexo (M/F)  
#• Salário  
#Ao final, o programa deve exibir: 
#• Média salarial  
#• Maior e menor idade  
#• Quantidade de clientes do sexo feminino com salário acima de R$ 3.000  
#• Percentual de clientes com idade acima de 50 anos 

#declaração de variáveis
repeticoes = 3
salarios = 0
maior_idade = 0
menor_idade = None
quantidade_feminino = 0
quantidade_acima_50 = 0

#loop para cadastro dos clientes
for i in range(repeticoes):
  if i >= repeticoes:
    break
  else:
    #while para pegar idade, validar e definir valores com base na idade
    while True:
     idade = input('Digite a idade do cliente: ')
     #if que verifica se é um número, caso contrário, pede para digitar novamente retornando para o inicio do while
     if not idade.isdigit():
      print('Digite um número válido!')
      continue #retorna para o inicio do while se entrar nesse if
     
     #Define Maior Idade
     if int(idade) > maior_idade: 
      maior_idade = int(idade)
  
     #Define Menor Idade
     if menor_idade is None or int(idade) < menor_idade:
       menor_idade = int(idade)
      
     #Define Maior que 50
     if int(idade) > 50:
       quantidade_acima_50 += 1
     break
    
    #while para pegar sexo...
    while True:
     sexo = input('Digite seu sexo(M/F): ')

     #if para verificar se digitou um genero válido ou não
     if sexo != 'M' and sexo != 'F':
       print("Digite um sexo válido(M/F)!")
       continue
     
     break
   
    #while para pegar salario
    while True:
     salario = input('Digite seu salário(ex: 1500): ').replace(',', '.', 1)

     #checar numero digitado pelo usuario
     if not salario.replace(".", "", 1).isdigit():
       print("Digite um número válido!")
       continue
     
     #checar se é mulher e ganha mais de 3000
     if float(salario) > 3000 and sexo == 'F':
       quantidade_feminino += 1
     
     #incrementar salarios para tirar a média depois
     salarios += float(salario)
     break
 
    print('Cliente Cadastrado!\n')
    
#print com resultados
print(f"""📊Resultado da análise dos {repeticoes} clientes:
💸Média salarial: {(salarios/repeticoes):.2f};
🧓Maior Idade: {maior_idade};
🧒Menor Idade: {menor_idade};
👩Mulheres com salario maior que R$ 3.000: {quantidade_feminino};
🧔Clientes com idade acima de 50 anos: {quantidade_acima_50};   
""")