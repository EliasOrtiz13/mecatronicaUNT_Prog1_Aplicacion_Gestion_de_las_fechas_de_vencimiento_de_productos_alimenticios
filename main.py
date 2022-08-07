import lector_barcode as lecbar
import fechas
import conexion_base_datos as cbd

try:
    cbd.createDB()
    cbd.createTable()
except:
    pass

# Datos que ingresa el usuario

codigo_barras = lecbar.lector_barcode()

marca = input('Ingrese marca: ').upper()
while len(marca) == 0:
    marca = input('Ingrese marca: ').upper()

nombre = input('Ingrese nombre: ').upper()
while len(nombre) == 0:
    nombre = input('Ingrese nombre: ').upper()

descripcion = input('Ingrese descripcion: ').upper()
while len(descripcion) == 0:
    descripcion = input('Ingrese descripcion: ').upper()

f_creacion = fechas.fecha_hoy_text().upper()

while True:
    try:
        dia = int(input('Ingrese dia: '))
        while dia<1 or dia>31:
            dia = int(input('Ingrese dia: '))
        break
    except:
        continue

while True:
    try:
        mes = int(input('Ingrese mes: '))
        while mes<1 or mes>12:
            mes = int(input('Ingrese mes: '))
        break
    except:
        continue

while True:
    try:
        año = int(input('Ingrese año: '))
        while año<2022 or len(str(año))!=4:
            año = int(input('Ingrese año: '))
        break
    except:
        continue

f_vencimiento = fechas.formato_fecha_text(dia, mes, año)

# Guardar datos en SQLite
cbd.inserta_producto(codigo_barras, marca, nombre, descripcion, f_creacion, f_vencimiento)
