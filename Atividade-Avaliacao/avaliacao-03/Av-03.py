def primo(p):
    contador = 0
    for i in range (1,p+1):
        if p%i==0:
            contador = contador+1
    if  contador==2:
        return True
    else:
        return False

def somador(n): 
    contador = 0
    soma = 0
    inputNum = 2
    primos = []
    while True:
        if primo(inputNum):
            contador = contador + 1
            soma = soma + inputNum
            primos.append(inputNum)
        inputNum = inputNum + 1
        if contador == n:
            break
    return (soma,primos)

inputNum = input("Por favor! Digite um número, sendo ele Inteiro e também não Negativo:")
soma, parcela = somador(int(inputNum))
if int(inputNum) >= 0:
    print("Se n for = {0}, logo, o resultado será {s}, sendo {p}. ".format(int(inputNum), s= soma, p = parcela))