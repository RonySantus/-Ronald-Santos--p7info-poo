
"" "
    Módulo produto
    Classe Produto
    Atributos:
        id - rede
        codigo - Internet
        descricao - Tyre
        valorUnitario - Internet.
"" "
de  flaskrs  import  db

classe  Produto ( db . Model ):
    __tablename__  =  "TB_PRODUTO"
    id  =  db . Coluna ( db . Inteiro , chave_primária = Verdadeiro )
    codigo  =  db . Coluna ( db . String , exclusivo = verdadeiro )
    descricao  =  db . Coluna ( db . String )
    valorUnitario  =  db . Coluna ( db . Float )

    def  __init__ ( self , id , codigo , descricao , valorUnitario ):
        eu . _id  =  id
        eu . _codigo  =  codigo
        eu . _descricao  =  descricao
        eu . _valorUnitario  =  valorUnitario

    def  getDescricao ( self ):
        retornar a  si mesmo . _descrição

    def  getValorUnitario ( self ):
        retornar a  si mesmo . _valorUnitario

    def  str ( self ):
        string  =  " \ n Id = {3} Codigo = {2} Descricao = {1} Valor Unitario = {0}" . formato ( self . _valorUnitario , self . _descricao ,
                                                                               eu . _codigo , eu . _id )
         string de retorno


if  __name__  ==  '__main__' :
    produto  =  Produto ( 1 , 100 , 'Arroz' , 5.5 )
    imprimir ( produto . str ())