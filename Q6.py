#Nome: Matheus Augusto Gomes da Silva
#Matrícula: 01894714
#--------------------------------------
#Uma loja deseja registrar suas vendas do dia. Crie um programa que: 
#• Permita inserir o valor de várias vendas.  
#• O programa deve parar quando o valor digitado for 0.  
#• Ao final, exiba:  
#o Total vendido no dia  
#o Quantidade de vendas realizadas  
#o Média das vendas 

total = 0
quantidade = 0

while True:
    valor = float(input("Digite o valor da venda (0 para encerrar): "))

    if valor == 0:
        break

    total += valor
    quantidade += 1

# Evitar divisão por zero
if quantidade > 0:
    media = total / quantidade
else:
    media = 0

print("\n--- Resultado do dia ---")
print(f"Total vendido: R$ {total:.2f}")
print(f"Quantidade de vendas: {quantidade}")
print(f"Média das vendas: R$ {media:.2f}")