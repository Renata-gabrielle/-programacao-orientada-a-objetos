
Renata Gabrielle Augusto Maia
Jogo de adivinhação

print("********* Adivinha Número *********")

numero_secreto = 4

chute = input("Digite seu chute:")

chute_inteiro = int(chute)

print("Seu chute eh:", chute)

if(chute_inteiro == numero_secreto):
	print("Você acertou")
else:
	print("Você errou")

