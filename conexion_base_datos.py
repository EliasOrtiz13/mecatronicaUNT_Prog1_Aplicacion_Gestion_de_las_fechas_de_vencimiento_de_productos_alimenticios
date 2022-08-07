import sqlite3 as sql

# Crear una base de datos
def createDB():
    conn = sql.connect("base_datos_productos.db")
    conn.commit()   # Ejecutar los cambios 
    conn.close()    # Cerrar conexión

# Crear una tabla. 
def createTable():
    conn = sql.connect("base_datos_productos.db")
    cursor = conn.cursor()
    # Colocamos dentro del parentesis 
    # el nombre de apartado con el tipo de argumento    
    cursor.execute(
        """CREATE TABLE productos_data (
           CODIGO text,
           MARCA text,
           NOMBRE text,
           DESCRIPCION text,
           F_CREACION text,
           F_VENCIMIENTO text
        )"""
    )
    conn.commit()    
    conn.close()   

def inserta_producto(codigo, marca, nombre, descripcion, f_creacion, f_vencimiento):
    conn = sql.connect("base_datos_productos.db")
    cursor = conn.cursor()
    bd = '''INSERT INTO productos_data (CODIGO, MARCA, NOMBRE, DESCRIPCION, F_CREACION, F_VENCIMIENTO)
    VALUES({}, '{}', '{}', '{}', '{}', '{}')'''.format(codigo, marca, nombre, descripcion, f_creacion, f_vencimiento)
    cursor.execute(bd)
    conn.commit()
    conn.close() 

def mostrar_productos():
    conn = sql.connect("base_datos_productos.db")
    cursor = conn.cursor()
    bd = "SELECT * FROM productos_data"
    cursor.execute(bd)
    registro = cursor.fetchall()
    conn.commit()
    conn.close() 
    return registro


if __name__ == "__main__":
    #createDB()
    #createTable()
    print(mostrar_productos())