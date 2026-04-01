#Nome: Thiago Henrique Pereira
#Matrícula: 01892849
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

senha_secreta = random.randint(1, 100)

pergunta01 = int(input("Tente acertar a senha secreta de 1 a 100: "))

while not pergunta01 == senha_secreta:
    pergunta01 = int(input("A senha secreta está incorreta, tente novamente: "))
else:
    print(f"Você acertou a senha secreta: {senha_secreta}")


