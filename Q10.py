#Nome: Matheus Augusto Gomes da Silva
#Matrícula: 01894714
#--------------------------------------
#Um supermercado deseja controlar o estoque de um produto. Crie um programa que: 
#• Inicie com uma quantidade em estoque (definida pelo usuário).  
#• Em seguida, registre saídas de produtos (vendas) até que seja digitado 0.  
#• A cada venda, o estoque deve ser atualizado.  
#Regras: 
#• Se o estoque ficar abaixo de 10 unidades, exibir: 
#"Estoque baixo! Repor imediatamente."  
#• Se o estoque chegar a 0, encerrar o programa automaticamente.

nomeProduto = input("✏️ Digite o nome do produto: ")#pegar nome do produto

#while para pegar estoque de produtos e já validar se é um numero ou não
while True: 
 estoqueString = input(f'🔄 Digite o número em estoque de {nomeProduto}: ').strip()
 if not estoqueString.isdigit():
  print('⁉️ Erro: Digite um valor válido.')
  continue
 
 estoque = int(estoqueString)
 break

#logica geral do codigo, while para 
while estoque > 0:#checar se estoque é menor que zero
 
 if estoque <= 10:#avisar caso estoque seja menor ou igual a 10
   print("❗Estoque baixo! Repor imediatamente.")

 print(f"📊 Estoque de {nomeProduto}: {estoque}")

 opcao = input("❔ Digite 1 para registrar uma venda ou 0 para alterar estoque: ")
 #escolher oque usuario quer fazer

 if not opcao == '1' and not opcao == '0':
  print('⁉️ Erro: Digite uma opção válida.')
  continue

 if opcao == '1':#caso queira registrar venda
  quantidade = int(input("💲Digite a quantidade vendida: "))
  if quantidade > estoque:#evitar que estoque fique negativo
   print("⁉️ Erro: Quantidade insuficiente em estoque.")
   continue
  estoque -= quantidade#subtrair estoque
  
 else:#caso queira alterar numero de estoque
  novoEstoque = int(input("🔄 Digite o novo estoque: "))
  print(f'✔️ Novo estoque: {novoEstoque}')
  estoque = novoEstoque

print('Estoque no fim. 😭😭😭')

  
