classe  Fila ():
    
    def  __init__ ( self ):
        eu . fila  = []
        
    def  inserir ( self , elemento ):
        eu . fila . anexar ( elemento )
        
    def  retirar ( self ):
        Se  len ( auto . fila ) >  0 :
            del  self . fila [ 0 ]
    
    def  vazia ( self ):
        retornar a  si mesmo . fila  == []
    
    def  mostrarFila ( self ):
        imprimir ( auto . fila )
        
pt  =  Fila ()

para  p  no  intervalo ( 3 ):
    pt . inserir ( p )
    
pt . mostrarFila ()
pt . inserir ( 3 )
pt . mostrarFila ()
pt . retirar ()
pt . mostrarFila ()

para  p  no  intervalo ( 5 ):
    pt . retirar ()

pt . mostrarFila ()