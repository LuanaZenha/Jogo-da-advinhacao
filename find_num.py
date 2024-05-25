"""
Crie um programa que gere um número compreendido entre 1 e 100 e guarde em memória. 
Depois disso, solicite ao usuário que tente adivinhar o número escolhido pelo computador. 
Quando o número for adivinhado, o usuário será notificado do acerto.

Em tempo, o usuário tem direito a tentar apenas 10 vezes.
"""

# Primeiro tenho que gerar um programa que guarde os numeros de 1 a 100
import random

lista = list(range(1, 101)) # Faz uma lista entre 1 e 101
numero_oculto = random.choice(lista) # Vai escolher um número dentro dessa lista
tentativas_max = 10

print("Quer jogar um jogo? Você terá 10 tentativas, caso falhe terá uma surpresa!")
print("Você está disposto a olhar profundamente para dentro de si mesmo e fazer as escolhas necessárias para sobreviver?")

while tentativas_max > 0: 
        print(f"Você tem {tentativas_max} tentativas restantes.")
        tentativa = int(input("Digite aqui o número escolhido entre 1 e 100: "))

        if tentativa < 1 or tentativa > 100:
            print("Tente novamente, escolha inválida, escolha apenas números entre 1 e 100")
            continue # Vai continuar o código após o erro criando essa excessão
        
        if tentativa == numero_oculto:
            print("Humm espertinho, você acertou!")
            break # Vai parar o loop do código, o usuário acertou
            
        if tentativa < numero_oculto:
            print("Tente novamente, você só tem mais algumas chances! (Uma dica, o número é maior)")
        
        else:
            print("Tente novamente, você só tem mais algumas chances! (Uma dica, o número é menor)")
    
        tentativas_max -= 1 

if tentativas_max == 0:
    print(f"Alguns são tão ingratos por estarem vivos, mas você não, não mais. O número era: {numero_oculto}")

