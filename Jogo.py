print("***************************")
print("Bem vindo ao jogo da velha!")
print("***************************")

tabuleiro = [['x/y', '1', '2', '3'],['1', '_', '_', '_'],['2', '_', '_', '_'],['3', '_', '_', '_']]

for x in tabuleiro:
    print(x)

fechou = False
vez = "X"

while (not fechou):

    print (f"Agora é vez de {vez}")
    x = int (input ("Insira x (Entre 1 e 3)"))
    y = int (input ("Insira y (Entre 1 e 3)"))

    if (tabuleiro[x][y] == "_"): #Verifica se a casa já não foi marcada
        tabuleiro[x][y] = vez
    else:
        print("Coordenada inválida")
        continue

    for x in tabuleiro:
        print(x)

    if (tabuleiro[1][1]==vez and tabuleiro[1][2]==vez and tabuleiro[1][3]==vez): #Condições de vitória
        print(f"{vez} venceu!")
        break
    if (tabuleiro[2][1]==vez and tabuleiro[2][2]==vez and tabuleiro[2][3]==vez):
        print(f"{vez} venceu!")
        break
    if (tabuleiro[3][1]==vez and tabuleiro[3][2]==vez and tabuleiro[3][3]==vez):
        print(f"{vez} venceu!")
        break
    if (tabuleiro[1][1]==vez and tabuleiro[2][1]==vez and tabuleiro[3][1]==vez):
        print(f"{vez} venceu!")
        break
    if (tabuleiro[1][2]==vez and tabuleiro[2][2]==vez and tabuleiro[3][2]==vez):
        print(f"{vez} venceu!")
        break
    if (tabuleiro[1][3]==vez and tabuleiro[2][3]==vez and tabuleiro[3][3]==vez):
        print(f"{vez} venceu!")
        break
    if (tabuleiro[1][1]==vez and tabuleiro[2][2]==vez and tabuleiro[3][3]==vez):
        print(f"{vez} venceu!")
        break
    if (tabuleiro[1][3]==vez and tabuleiro[2][2]==vez and tabuleiro[3][1]==vez):
        print(f"{vez} venceu!")
        break                                                                   #Condições de vitória\

    i = 0  # Condição que detecta empate
    teste = ['_', '_', '_', '_']
    for x in tabuleiro:
        teste[i] = ("_" in x)
        i += 1
    if (not teste[1] and not teste[2] and not teste[3]):
        print("Empate!")
        fechou = True  # Condição que detecta empate\

    if (vez == "X"): #Passa a vez
        vez = "O"
    else:
        vez = "X"

