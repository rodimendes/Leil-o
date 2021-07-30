from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

def verificador(verificador_vencedor):
    """Retorna o maior valor e o respectivo apostador
    """
    maior = 0
    apostador = ""

    for pessoas in apostadores:
        if apostadores[pessoas] > maior:
            maior = apostadores[pessoas]
            apostador = pessoas
    return apostador, maior

print(art.logo)
print("Bem-vindo à casa de leilões.")

apostadores = {}

continuar = True
while continuar:
    nome = input("Qual seu nome?: ")
    aposta = int(input("Qual sua aposta? $"))
    apostadores[nome] = aposta
    resposta = input("Mais algum apostador? Type 'sim' or 'não'\n").lower()
    if resposta[0] == 'n':
        continuar = False
    else:
        clear()
        
print(f"A maior aposta foi de {verificador(apostadores)[0]}, no valor de ${verificador(apostadores)[1]}")