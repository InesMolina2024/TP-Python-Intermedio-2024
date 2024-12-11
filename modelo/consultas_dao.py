from .conecciondb import ConeccionDB

def crear_tabla():
    conn = ConeccionDB()

    sql= f'''
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );

        CREATE TABLE IF NOT EXISTS Director(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(10),
        Apellido VARCHAR(20),
        PRIMARY KEY (ID AUTOINCREMENT),
        );

        CREATE TABLE IF NOT EXISTS Peliculas(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),
        Genero INTEGER,
        Director INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT),
        FOREIGN KEY (Genero) REFERENCES Genero(ID),
        FOREIGN KEY (Director) REFERENCES Director(ID)
        );
        
     '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


class Peliculas():

    def __init__(self,nombre,director,duracion,genero):
#
       self.id= peliculas= None
       self.nombre = nombre
       self.director = director
       self.duracion = duracion 
       self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.director},{self.duracion},{self.genero}]'
#
def guardar_peli(pelicula):
    conn = ConeccionDB()
#
    sql= f'''
        INSERT INTO Peliculas(Nombre,Director,Duracion,Genero)
        VALUES('{pelicula.nombre}',{pelicula.director},'{pelicula.duracion}',{pelicula.genero});
'''
   # 
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
         pass

def listar_peli():
    conn = ConeccionDB()
    listar_peliculas = []
#
    sql= f'''
        
        SELECT * FROM Peliculas as p
        INNER JOIN Genero as g
        ON p.Genero = g.ID
        INNER JOIN Director as d
        ON p.Director = d.ID;
             
'''
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()
        return listar_peliculas
    except:
        pass


def listar_generos():
    conn = ConeccionDB()
    listar_generos = []

    sql= f'''
        SELECT * FROM Genero;
'''
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except:
        pass
    
def listar_director():
    conn = ConeccionDB()
    listar_director = []

    sql= f'''
        SELECT CONCAT(Nombre, ' ', Apellido) FROM Director;
'''
    try:
        conn.cursor.execute(sql)
        listar_director = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_director
    except:
        pass
    

def editar_peli(pelicula, id):
    conn = ConeccionDB()

    sql= f'''
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', Director = '{pelicula.director}', Duracion = '{pelicula.duracion}', Genero = {pelicula.genero}
        WHERE ID = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def borrar_peli(id):
    conn = ConeccionDB()

    sql= f'''
        DELETE FROM Peliculas
        WHERE ID = {id};
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass