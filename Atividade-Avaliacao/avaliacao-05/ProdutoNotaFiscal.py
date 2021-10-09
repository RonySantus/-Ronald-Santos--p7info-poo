"" "
"" "

de  notaFiscal  importação  NotaFiscal
from  product  import  Produto


classe  NotaFiscal_Produto ():

    def  _init_ ( self ):
        eu . _notasFiscais  = []
        eu . _produtos  = []

    def  adicionarNotaProduto ( self , nota , produto ):
        se  isinstance ( nota , NotaFiscal ) e  isinstance ( produto , Produto ):
            eu . _notasFiscais . anexar ( nota )
            eu . _produtos . anexar ( produto )