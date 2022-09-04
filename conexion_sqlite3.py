import sqlite3 as sql
from datetime import datetime
import fechas

# Crear una base de datos
def createDB():
    conn = sql.connect("base_datos_productos.db")
    conn.commit()
    conn.close()

    # Crear una tabla. 
def createTable():
    conn = sql.connect("base_datos_productos.db")
    cursor = conn.cursor()
    # Colocamos dentro del parentesis 
    # el nombre de apartado con el tipo de argumento    
    cursor.execute(
        """CREATE TABLE productos_data (
        CODIGO integer,
        MARCA text,
        NOMBRE text,
        DESCRIPCION text,
        F_CREACION text,
        F_VENCIMIENTO text
        )"""
    )
    conn.commit()    # Ejecutar los cambios 
    conn.close()    # Cerrar conexión

class Comunicacion():
    
    def __init__(self):
        self.conexion = sql.connect('base_datos_productos.db')

    def recorrer_rows(self):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM productos_data ORDER BY NOMBRE DESC'''
        resultado = cursor.execute(bd)

        self.conexion.commit()
        
        return resultado

# ==============================================================

    def leer_rows(self):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM productos_data'''
        cursor.execute(bd)
        datos = cursor.fetchall()
        self.conexion.commit()
        cursor.close()
        return datos

# ==============================================================

    def insertar_producto(self, codigo, marca, nombre, descripcion, f_creacion, f_vencimiento):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO productos_data (CODIGO, MARCA, NOMBRE, DESCRIPCION, F_CREACION, F_VENCIMIENTO)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(codigo, marca, nombre, descripcion, f_creacion, f_vencimiento)
        cursor.execute(bd)
        self.conexion.commit() 
        cursor.close()

    def eliminar_producto(self, codigo):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM productos_data WHERE CODIGO = "{}"'''.format(codigo)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()


    def actualizar_producto(self, codigo, marca, nombre, descripcion, f_vencimiento):
        cursor = self.conexion.cursor()
        bd = '''UPDATE productos_data SET MARCA ='{}', NOMBRE ='{}', DESCRIPCION ='{}', F_VENCIMIENTO = '{}'
        WHERE CODIGO = '{}' '''.format(marca, nombre, descripcion, f_vencimiento, codigo)
        cursor.execute(bd)
        cursor.rowcount
        self.conexion.commit()
        cursor.close()
        

if __name__ == "__main__":
    
    leer = Comunicacion()
    datos = leer.leer_rows() # lista