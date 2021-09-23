composição = 0
separar = "-"
while True:
    frase = input("Digite a frase desejada: ").split()
    tamanho = []
    
    for r in frase:
        tamanho.append(str(len(r)))
        if len(r) >= composição:
            composição = len(r)
            maiorPalavra = r
    print(separar.join(tamanho))

    end = str(input("Digite ENTER para prosseguir com o programa ou 0 para encerrá-lo:"))
    if end == "0":
        break

print()
print("A maior palavra é: %s" % maiorPalavra)