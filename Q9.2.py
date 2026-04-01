#Nome: Guilherme Fortaleza de Souza
#Matrícula: 01877047
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

# função para verificar se é maior ou menor de idade

def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade" 
    elif idade < 18:
        return "Menor de idade"
    
# variáveis...

soma_slarios = 0
mulheres_salario3000 = 0
acima_50 = 0

# cadastro dos usuarios e a quantidade 

for i in range(20):
    idade = int(input("Digite a idade do funcionário: "))
    salario = float(input("Digite o salário do funcionário: "))
    sexo = input("Digite o sexo do funcionário (M/F): ").upper()

# soma dos salários para calcular a média depois
    soma_slarios = soma_slarios + salario

# verificações para contar as mulheres com salário acima de 3000  as pessoas acima de 50 anos
    
    if sexo == 'F' and salario > 3000:
        mulheres_salario3000 += 1
        print(verificar_idade(idade))

    elif idade >= 18: 
        print(verificar_idade(idade))
    if idade > 50:
        acima_50 += 1
    else:
        print(verificar_idade(idade))

# impressão dos resultados dos dados

media_salarios = soma_slarios / 20
print(f"Média dos salários: {media_salarios:.2f}")
print(f"Quantidade de mulheres com salário acima de R$3000: {mulheres_salario3000}")
print(f"Quantidade de pessoas acima de 50 anos: {acima_50}")
