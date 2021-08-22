def somaImposto(taxaImposto, custo):
    resultado = (taxaImposto / 100) * custo + custo    
    return resultado

print("Digite a taxa de imposto:")
taxaImposto = float(input())
print("Digite o custo:")
custo = float(input())
print("O valor do seu produto é: " + str(somaImposto(taxaImposto, custo)))