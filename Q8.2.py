#Nome: Gustavo Nascimento da Silva
#Matrícula: 01866201
#--------------------------------------
#Crie um programa onde: 
#• O sistema define um número secreto entre 1 e 100.  
#• O usuário tenta adivinhar.  
#• O programa deve continuar até o usuário acertar.  
 
#Durante o jogo: 
#• Informe se o número digitado é maior ou menor que o número secreto.  
#• Ao final, exiba:  
#o Quantidade de tentativas  
#o Mensagem de desempenho (ex: “Excelente”, “Bom”, “Tente melhorar”) 

import random

# Gerar número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
acertou = False

print("=== Jogo de Adivinhação ===")
print("Tente adivinhar o número entre 1 e 100!")

while not acertou:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é MAIOR que isso.")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR que isso.")
    else:
        acertou = True
        print("\nParabéns! Você acertou o número!")

# Avaliação de desempenho
print(f"\nQuantidade de tentativas: {tentativas}")

if tentativas <= 5:
    print("Desempenho: Excelente!")
elif tentativas <= 10:
    print("Desempenho: Bom!")
else:
    print("Desempenho: Tente melhorar!")