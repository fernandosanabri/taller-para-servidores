from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,
    String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


engine = create_engine( 'mysql+pymysql://root:Admin1234@localhost/taller1' )
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



class Alumno(Base):
    __tablename__ = 'alumnos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), index=True, nullable=False)
    apellido = Column(String(30))
    cedula = Column(String(13))
    
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def __repr__(self):
        return unicode(self.nombre)


class Profesor(Base):
    __tablename__ = 'profesores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre


class Asistencia(Base):
    __tablename__ = 'Asistencias'
    id = Column(Integer, primary_key=True)
    alumno = Column(String(50), nullable=False)
    profesor = Column(String(50), nullable=False)
    curso = Column(String(120), nullable=False)
    
    def __init__(self, alumno, profesor, curso):
        self.alumno = alumno
        self.profesor = profesor
        self.curso = curso

Base.metadata.create_all(engine)