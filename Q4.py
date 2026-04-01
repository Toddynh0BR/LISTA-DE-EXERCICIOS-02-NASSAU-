#Nome: Gustavo Nascimento da Silva
#Matrícula: 01866201
#--------------------------------------
#Escreva  um  algoritmo  para  ler  dois  valores.  Após  a  leitura  deve-se  calcular  a  soma  dos  valores  lidos  e 
#armazená-la  em  uma  variável.  Após  o  cálculo  da  soma,  escrever  o  resultado  e  escrever  também  a  pergunta 
#'Novo Cálculo (S/N)?'. Deve-se ler a resposta  e se a resposta for 'S' (sim), deve-se repetir todos os comandos  
#(instruções)  novamente,  mas  se  a  resposta  for  'N'  (não),  o  algoritmo  deve  ser  finalizado  escrevendo  a 
#mensagem ‘Fim dos Cálculos‘.

resposta = "S"

while resposta == "S":
     # Ler os dois valores
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

     # Calcular a soma
    soma = valor1 + valor2

     # Mostrar o resultado
    print("Resultado da soma:", soma)

     # Perguntar se deseja novo cálculo
    resposta = input("Novo cálculo (S/N)? ").upper()

# Mensagem final
print("Fim dos Cálculos")