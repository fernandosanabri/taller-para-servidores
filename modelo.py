
from sqlalchemy import create_engine
from connector import *
# conexion
#engine = create_engine('sqlite:///libros.db', echo=True)
#engine = create_engine( 'mysql+pymysql://root:Admin1234@localhost/taller1' )
# sesion


# insertamos autores
autor_1 = Asistencia('lola garcia','jose garcia','programacion')
autor_2 = Asistencia('pedro zuares','jose garcia','etica')
autor_3 = Asistencia('pedro zuares','jose garcia','calculo')
autor_4 = Asistencia('pedro zuares','jose garcia','istoria')
autor_5 = Asistencia('pedro zuares','jose garcia','etica')
autor_6 = Asistencia('pedro zuares','jose garcia','dibujo')
autor_7 = Asistencia('pedro zuares','jose garcia','geografia')
autor_8 = Asistencia('pedro zuares','jose garcia','ingles')
lista_autores = (autor_1, autor_2,autor_3, autor_4,autor_5, autor_6,autor_7, autor_8)
session.add_all(lista_autores)
session.commit()
