def calcularDeterminates(ordem, matriz):
    if ordem == 1:
        det = matriz[0]
        return det

    elif ordem == 2:
        diagonalPrincipal2 = matriz[0][0] * matriz[1][1]
        diagonalSecundaria2 = matriz[0][1] * matriz[1][0]
        det = diagonalPrincipal2 - diagonalSecundaria2
        return det

    elif ordem == 3:
        diagonaisPrincipais3 = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1])
        diagonaisSecundarias3 = (matriz[0][2] * matriz[1][1] * matriz[2][0]) + (matriz[0][0] * matriz[1][2] * matriz[2][1]) + (matriz[0][1] * matriz[1][0] * matriz[2][2])
        det = diagonaisPrincipais3 - diagonaisSecundarias3
        return det

matriz1 = [-7]
matriz2 = [[2,5],[-2,-5]]
matriz3 = [[ 1,2,5],[0,1,3], [-1,0,-2]]

print(calcularDeterminates(len(matriz1), matriz1))
print(calcularDeterminates(len(matriz2), matriz2))
print(calcularDeterminates(len(matriz3), matriz3))

    



