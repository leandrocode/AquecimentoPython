def somarMatriz(matrizA, matrizB):
    resultado = []
    for i in range(len(matrizA)):            
        resultado.append([])         
        for j in range(len(matrizA[0])):             
            resultado[i].append(matrizA[i][j] + matrizB[i][j])
    return resultado

def subtrairMatriz(matrizA, matrizB):
    resultado = []
    for i in range(len(matrizA)):            
        resultado.append([])         
        for j in range(len(matrizA[0])):             
            resultado[i].append(matrizA[i][j] - matrizB[i][j])
    return resultado

def multiplicarMatriz(matrizA, matrizB):
    linhaMatrizA = len(matrizA)              
    colunaMatrizB = len(matrizA[0])    
    resultado = []                       

    for i in range(linhaMatrizA):           
        resultado.append([])

        for j in range(colunaMatrizB):
            listaMultiplicada = [x*y for x, y in zip(getLinha(matrizA, i), getColuna(matrizB, j))]
            resultado[i].append(sum(listaMultiplicada))

    return resultado
       
def getLinha(matriz, n):
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    return [i[n] for i in matriz]    

def transpostarMatriz(matriz):
    return [list(i) for i in zip(*matriz)]

def multiplicarMatrizNumeroReal(matriz, numero):
    resultado = []
    for i in range(len(matriz)):            
        resultado.append([])         
        for j in range(len(matriz[0])):             
            resultado[i].append(matriz[i][j] * numero)
    
    return resultado 

def inverterMatriz(matriz):
    determinante = getMatrizDeterminante(matriz)
    if len(matriz) == 2:
        return [[matriz[1][1]/determinante, -1*matriz[0][1]/determinante],
                [-1*matriz[1][0]/determinante, matriz[0][0]/determinante]]

    cofatores = []
    for r in range(len(matriz)):
        cofatorLinha = []
        for c in range(len(matriz)):
            menor = getMatrizMenor(matriz, r, c)
            cofatorLinha.append(((-1)**(r + c)) * getMatrizDeterminante(menor))
        cofatores.append(cofatorLinha)
    cofatores = transpostarMatriz(cofatores)
    for r in range(len(cofatores)):
        for c in range(len(cofatores)):
            cofatores[r][c] = cofatores[r][c]/determinante
    return cofatores

def getMatrizMenor(matriz, i, j):
    return [linha[:j] + linha[j+1:] for linha in (matriz[:i] + matriz[i+1:])]

def getMatrizDeterminante(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    determinante = 0
    for c in range(len(matriz)):
        determinante += ((-1)**c) * matriz[0][c] * getMatrizDeterminante(getMatrizMenor(matriz, 0, c))
    return determinante


a = [[2, 1], [-3, 4]]
b = [[0, -1], [2, 5]]
c = [[3, 0], [6, 1]]

print("exercício 1: [A + (B - Ct)] * B =")
resultado1 = subtrairMatriz(b, transpostarMatriz(c))
resultado1 = somarMatriz(a, resultado1)
resultado1 = multiplicarMatriz(resultado1, b)
print(str(resultado1) + "\n")

print("exercício 2: (B + At) * C^-1 - (3 * Bt) =")
resultado2 = somarMatriz(b, transpostarMatriz(a))
inversaC = inverterMatriz(c)
resultado2 = multiplicarMatriz(resultado2, inversaC)
resultado2 = subtrairMatriz(resultado2, multiplicarMatrizNumeroReal(transpostarMatriz(b), 3))
print(resultado2)

