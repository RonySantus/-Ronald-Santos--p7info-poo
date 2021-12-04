"" "
    Módulo tipocliente -
    Classe TipoCliente - Enumeração de Tipos de Cliente
"" "

import  enum


classe  TipoClient ( enum . Enum ):
    PESSOA_FISICA  =  1
    PESSOA_JURIDICA  =  2


if  __name__  ==  '__main__' :
    print ( "Os numeros enum sao:" )
    para  tipo  em ( TipoClient ):
        imprimir ( tipo ( tipo ))
        imprimir ( tipo )