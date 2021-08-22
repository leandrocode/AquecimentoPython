def nomeVertical():
    print("Digite seu nome:")
    nome = list(str(input()))

    print("Esse é o seu nome na vertical:")
    for item in range(len(nome)):
        print(nome[item])

nomeVertical()