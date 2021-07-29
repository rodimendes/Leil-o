from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

def verificador(verificador_vencedor):
    maior = 0
    apostador = ""

    for pessoas in apostadores:
        if apostadores[pessoas] > maior:
            maior = apostadores[pessoas]
            apostador = pessoas
    return apostador, maior

print(art.logo)
print("Welcome to the secret auction program.")

apostadores = {}

continuar = True
while continuar:
    nome = input("What is your name?: ")
    bid = int(input("What's your bid? $"))
    apostadores[nome] = bid
    resposta = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if resposta[0] == 'n':
        continuar = False
    else:
        clear()
        
print(f"A maior aposta foi de {verificador(apostadores)[0]}, no valor de ${verificador(apostadores)[1]}")