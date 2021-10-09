"" "
    Módulo itemnotafiscal
    Classe ItemNotaFiscal
    Atributos:
        id - rede
        sequencial - Internet
        quantidade - rede
        produto - Internet
        valor - válida.
"" "
from  product  import  Produto


classe  ItemNotaFiscal ():

    def  _init_ ( self , id , sequencial , quantidade , produto ):
        eu . _id  =  id
        eu . _sequencial  =  sequencial
        eu . _quantidade  =  quantidade
        eu . _produto  =  produto
        eu . _descricao  =  self . _produto . getDescricao ()
        eu . _valorUnitario  =  self . _produto . getValorUnitario ()
        eu . _valorItem  =  float ( self . _quantidade  *  self . _valorUnitario )

    def  str ( self ):
        string  =  " \ n Id = {5} Sequencial = {4} Quantidade = {3} Produto = {2} Valor Unitario = {1} Valor Item = {0}" . formato (
            eu . _valorItem ,
            eu . _valorUnitario ,
            eu . _descrição ,
            eu . _quantidade ,
            eu . _sequencial ,
            eu . _id )
         string de retorno

    def  getId ( self ):
        retornar a  si mesmo . _Eu iria

    def  getvalorItem ( self ):
        retornar a  si mesmo . _valorItem

    def  getValorUnitario ( self ):
        retornar a  si mesmo . _valorUnitario

    def  getDescricao ( self ):
        retornar a  si mesmo . _descrição

    def  getQuantidade ( self ):
        retornar a  si mesmo . _quantidade

    def  getSequencial ( self ):
        retornar a  si mesmo . _sequencial

if  __name__  ==  '__main__' :
    produto  =  Produto ( 1 , 100 , 'Arroz' , 5.5 )
    item  =  ItemNotaFiscal ( 1 , 1 , 12 , produto )
    imprimir ( item . str ())
