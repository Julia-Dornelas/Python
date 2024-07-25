import os

# Função para mostrar o tabuleiro
def mostrarTabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            if j !=2:
                print(tabuleiro[i][j] + '|', end='')
            else:
                print(tabuleiro[i][j] + '\n')
        if i !=2:
            print('-'*10)

# Matriz para ser o tabuleiro
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

i = 0
while True:
    # Mostra tabuleiro a cada loop
    mostrarTabuleiro(tabuleiro)

    if i % 2 == 0:
        x, y  = [int(pos) for pos in input('Vez de jogador X: ').split()] 
        x -= 1
        y -= 1
    else:
        x, y  = [int(pos) for pos in input('Vez de jogador O: ').split()] 
        x -= 1
        y -= 1
    
    if tabuleiro[x][y] != ' ':
        print('Casa ja ocupada!!!')
        continue
    
    if i % 2 == 0:
        tabuleiro[x][y] = 'X'
    else:
        tabuleiro[x][y] = 'O'

#XIS
    #LINHA
    if tabuleiro [0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == 'X':
        print("Jogador X ganhou")
        break
    if tabuleiro [1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == 'X':
        print("Jogador X ganhou")
        break
    if tabuleiro [2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][2] == 'X':
        print("Jogador X ganhou")
        break
    #COLUNA
    if tabuleiro [0][0] == 'X' and tabuleiro[1][0] == 'X' and tabuleiro[2][0] == 'X':
        print("Jogador X ganhou")
        break
    if tabuleiro [0][1] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][1] == 'X':
        print("Jogador X ganhou")
        break
    if tabuleiro [0][2] == 'X' and tabuleiro[1][2] == 'X' and tabuleiro[2][2] == 'X':
        print("Jogador X ganhou")
        break
    #DIAGONAL
    if tabuleiro [0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X':
        print("Jogador X ganhou")
        break
    if tabuleiro [2][2] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[0][0] == 'X':
        print("Jogador X ganhou")
        break

    


#BOLA
        #LINHA
    if tabuleiro [0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == 'O':
        print("Jogador O ganhou")
        break
    if tabuleiro [1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][2] == 'O':
        print("Jogador O ganhou")
        break
    if tabuleiro [2][0] == 'O' and tabuleiro[2][1] == 'O' and tabuleiro[2][2] == 'O':
        print("Jogador O ganhou")
        break
    #COLUNA
    if tabuleiro [0][0] == 'O' and tabuleiro[1][0] == 'O' and tabuleiro[2][0] == 'O':
        print("Jogador O ganhou")
        break
    if tabuleiro [0][1] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][1] == 'O':
        print("Jogador O ganhou")
        break
    if tabuleiro [0][2] == 'O' and tabuleiro[1][2] == 'O' and tabuleiro[2][2] == 'O':
        print("Jogador O ganhou")
        break
    #DIAGONAL
    if tabuleiro [0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O':
        print("Jogador O ganhou")
        break
    if tabuleiro [2][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[0][0] == 'O':
        print("Jogador O ganhou")
        break

    i += 1
    os.system("cls")