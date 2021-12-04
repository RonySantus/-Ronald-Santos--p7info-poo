from  flask  importar  Flask
de  flask_sqlalchemy  importar  SQLAlchemy 

app  =  Flask ( __name__ )
db  =  SQLAlchemy ( app )

if  __name__  ==  "__main__" :
    app . run ()