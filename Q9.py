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
salarios = 0
maior_idade = 0
menor_idade = 0
quantidade_feminino = 0
quantidade_acima_50 = 0

#loop para cadastro dos clientes
for i in range(20):
  if i >= 20:
    break
  else:
    #while para pegar idade e validar
    while True:
     idade = input('Digite a idade do cliente: ')
     #if que verifica se é um número, caso contrário, pede para digitar novamente retornando para o inicio do while
     if not idade.isdigit():
      print('Digite um número válido!')
      continue  
      
     break
    
        
        
        
        
        
        
        
        
 