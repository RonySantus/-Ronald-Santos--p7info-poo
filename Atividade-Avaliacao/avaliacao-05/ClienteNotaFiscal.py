"" "
    Módulo cliente -
    Classe Cliente -
    Atributos:
        _id - chave primária - rede
        _nome - nome do cliente -.
        _codigo - codigo do cliente -.
        _cnpjcpf - cnpj ou cpf - Internet
        _tipo - tipo do cliente -.
                    (Pessoa Fisica ou Juridica)
"" "



classe  Cliente ():
    def  _init_ ( self , id , nome , codigo , cnpjcpf ):
        eu . _id  =  id
        eu . _nome  =  nome
        eu . _codigo  =  codigo
        eu . _cnpjcpf  =  cnpjcpf

    def  str ( self ):
        string  =  " \ n Id = {3} Codigo = {2} Nome = {1} CNPJ / CPF = {0}" . formato ( self . _cnpjcpf , self . _codigo ,
                                                                             eu . _nome , self . _id )
         string de retorno


if  __name__  ==  '__main__' :
    cliente  =  Cliente ( 1 , "Manoel Costa" , 100 , '200.100.345-34' )
    imprimir ( cliente . str ())