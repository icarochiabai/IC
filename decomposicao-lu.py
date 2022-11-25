# Matriz para ser decomposta
A = [
    [2, 3, 1, 1],
    [4, 7, 4, 3],
    [4, 7, 6, 4],
    [6, 9, 9, 8]
]

# Criação da matriz identidade associada
I = []
for i in range(len(A)):
    I.append([])
    for j in range(len(A[0])):
        if i == j:
            I[i].append(1)
        else:
            I[i].append(0)


# Inicializamos as matrizes U e L
U = A.copy()
L = I.copy()

# Algoritmo para decompor a matriz A
for j in range(len(U)):
    if U[j][j] == 0:
        print("Essa matriz não possui decomposição LU.")
        break
    for i in range(j + 1, len(U)):
        L[i][j] = U[i][j]/U[j][j]
        U[i][j] = 0
        for k in range(j + 1, len(U)):
            U[i][k] = U[i][k] - L[i][j] * U[j][k]

# Função para facilitar o display das matrizes
def mostrarMatriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(float(elemento), end=" ")
        print()
    print()


# Saída

print("A = LU, tal que:")

print("L:")
mostrarMatriz(L)
print("U:")
mostrarMatriz(U)