"" "
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos:
            id - rede.
            codigo - Internet.
            dados - Internet.
            cliente - Internet.
            itens - rede
            valornota - limites.
"" "
de  datetime  import  datetime
de  clienteNotaFiscal  import  Cliente
de  itemNotaFiscal  importar  ItemNotaFiscal


classe  NotaFiscal ():
    def  _init_ ( self , Id , codigo , cliente ):
        eu . _Id  =  Id
        eu . _codigo  =  codigo
        eu . _cliente  =  cliente
        eu . _data  =  datetime . hoje ()
        eu . _itens  = []
        eu . _valorNota  =  0,0

    def  setCliente ( self , cliente ):
        if  isinstance ( cliente , Cliente ):
            eu . _cliente  =  cliente
            retornar a  si mesmo . _cliente

    def  adicionarItem ( self , item ):
        if  isinstance ( item , ItemNotaFiscal ):
            eu . _itens . anexar ( item )

    def  calcularNotaFiscal ( self ):
        valor  =  0,0
        para o  item  em  si mesmo . _itens :
            valor  + =   item . _valorItem
        eu . valorNota  =  valor

    def  imprimirNotaFiscal ( self ):
        imprimir ( f '' '-------------------------------------------- -------------------------------------------------- -----
NOTA FISCAL \ t \ t \ t \ t  { self . _data }
Cliente: { self . _cliente . _codigo } \ t \ t \ t \ t Nome: { self . _cliente . _nome }
CPF / CNPJ: { self . _cliente . _cnpjcpf }
-------------------------------------------------- -------------------------------------------------
ITENS
-------------------------------------------------- -------------------------------------------------
Seq Descrição QTD Valor Unit Preço
---- ---------------------------------------------- ---------- ----- ------------ ------------------ '' ' )
        para  c  no  intervalo ( 0 , 3 ):
            print ( '{0: <17} {1: ^ 34} {2: ^ 28} {3: <8} {4}' . format ( self . _itens [ c ]. getSequencial (),   self . _itens [ c ]. getDescricao (), self . _itens [ c ]. getQuantidade (), self . _itens [ c ]. getValorUnitario (), self . _itens [ c ]. getvalorItem ()))

        imprimir ( 'Valor Total:' , self . valorNota )