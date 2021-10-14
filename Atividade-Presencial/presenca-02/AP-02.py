def  printDecimal ( num ):
    retornar  num

def  printOctal ( num ):
    retorno  oct ( num )

def  printHexadecimal ( num ):
    return  hex ( num )

def  printBinario ( num ):
     caixa de retorno ( num )

def  imprimirTabela ():
    print ( "{: ^ 14} {: ^ 14} {: ^ 30} {: ^ 13}" . formato ( "Decimal" , "Octal" , "Hexadecimal" , "Binario" ))
    print ( "------------- \ t --------- \ t --------------------- \ t ----------------- " )
    para  cont  no  intervalo ( 0 , 255 + 1 ):
        print ( "{: ^ 14} {: ^ 14} {: ^ 30} {: ^ 13}" . format ( printDecimal ( cont ), printOctal ( cont ), printHexadecimal ( cont ), printBinario ( cont )))
        
imprimir ( imprimirTabela ())