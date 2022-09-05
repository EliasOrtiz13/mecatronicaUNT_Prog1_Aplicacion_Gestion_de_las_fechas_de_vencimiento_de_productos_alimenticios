from tkinter import messagebox, ttk
from tkinter import *
import lector_barcode as barcode
import fechas
from conexion_sqlite3 import Comunicacion
from comparar import Comparar
from g_mail import EnviarEmail

class AppProductos:
    
    db_name = 'base_datos_productos.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('App de productos')
        
        # clase comunicacion sqlite
        self.base_datos = Comunicacion()
        # clase comparar
        self.comparar = Comparar()
        # clase conexion g_mail
        self.g_mail = EnviarEmail()

        # ======================= Frame contenedor 1 ===========================
        frame1 = LabelFrame(self.wind, text = 'DATOS DEL USUARIO')
        frame1.grid(row=0, column=0, columnspan=3, pady=15)
        frame1.configure(font=("Arial", 12, "italic"))

        # Nombre de usuario
        Label(frame1, text='Nombre: ').grid(row=1, column=0, pady=2)
        self.nombre_user = Entry(frame1)
        self.nombre_user.grid(row=1, column=1)

        # Correo electronico
        Label(frame1, text='Correo Gmail: ').grid(row=2, column=0, pady=2)
        self.correo_user = Entry(frame1)
        self.correo_user.grid(row=2, column=1)

        # Button Recibir estado de productos
        ttk.Button(frame1, text='Recibir estado de productos', command=self.alarmas).grid(row=3, column=0, columnspan=3,pady=6)

        # Mensaje
        self.mensaje_user = Label(frame1, text = '', fg='blue')
        self.mensaje_user.grid(row=4, column=0, columnspan=3, sticky=W+E)


        # ======================= Frame contenedor 2 ===========================
        frame2 = LabelFrame(self.wind, text = 'REGISTRAR NUEVO PRODUCTO')
        frame2.grid(row=4, column=0, columnspan=3, pady=15)
        frame2.configure(font=("Arial", 12, "italic"))
                
        # Seleccionar cámara:
        Label(frame2, text="Seleccionar cámara:", fg="black").grid(row=5, column=0)
        self.opcion_seleccionada = IntVar()
        opc1 = ttk.Radiobutton(frame2, text='Principal', variable=self.opcion_seleccionada, value=1)
        opc1.grid(row=5, column=1)
        opc2 = ttk.Radiobutton(frame2, text='Externa', variable=self.opcion_seleccionada,  value=2)
        opc2.grid(row=5, column=2)

        # Codigo Input
        ttk.Button(frame2, text='Escanear Código', command=self.obtener_barcode).grid(row=6, column=0, pady=6, sticky=W+E)
        Label(frame2, text='Presionar ESC para salir', fg='brown').grid(row=6, column=1, pady=2)     
        Label(frame2, text='Código: ').grid(row=7, column=0, pady=2)
        self.codigo_label = Label(frame2, text = '', fg='blue')
        self.codigo_label.grid(row=7, column=1)

        # Marca Input
        Label(frame2, text='Marca: ').grid(row=8, column=0, pady=2)
        self.marca = Entry(frame2)
        self.marca.grid(row=8, column=1)

        # Nombre Input
        Label(frame2, text='Nombre: ').grid(row=9, column=0, pady=2)
        self.nombre = Entry(frame2)
        self.nombre.grid(row=9, column=1)

        # Descripcion Input
        Label(frame2, text='Descripción: ').grid(row=10, column=0, pady=2)
        self.descripcion = Entry(frame2)
        self.descripcion.grid(row=10, column=1)

        # F_creacion Input
        Label(frame2, text='Fecha creación: ').grid(row=11, column=0, pady=2)
        self.f_creacion = fechas.fecha_hoy_text()
        self.f_creacion_label = Label(frame2, text=self.f_creacion, fg='blue').grid(row=11, column=1)

        # F_vencimiento
        Label(frame2, text='Fecha vencimiento: ').grid(row=12, column=0, pady=2)
            # dia
        Label(frame2, text='Dia: ').grid(row=13, column=0, pady=2)
        self.dia = Entry(frame2)
        self.dia.grid(row=14, column=0)
            # mes
        Label(frame2, text='Mes: ').grid(row=13, column=1, pady=2)
        self.mes = Entry(frame2)
        self.mes.grid(row=14, column=1)
            # año
        Label(frame2, text='Año: ').grid(row=13, column=2, pady=2)
        self.año = Entry(frame2)
        self.año.grid(row=14, column=2)
        
        # Button Add Producto
        ttk.Button(frame2, text='Guardar producto', command=self.agregar_productos).grid(row=15, column=1, pady=6)

        # Mensaje de salida 1
        self.mensaje = Label(frame2, text = '', fg='red')
        self.mensaje.grid(row=16, column=0, columnspan=3, sticky=W+E)


        # ====================== Frame contenedor 3 ======================================
        frame3 = LabelFrame(self.wind, text = 'DATOS GENERALES DEL INVENTARIO')
        frame3.grid(row=0, column=3, columnspan=6, pady=15)
        frame3.configure(font=("Arial", 12, "italic"))

        # Total productos
        Label(frame3, text='Productos registrados: ', fg='blue').grid(row=1, column=3, pady=2)
        self.total_prod = Label(frame3, text = '', fg='brown')
        self.total_prod.grid(row=1, column=4)

        # Proximos a f_vencimiento
        Label(frame3, text='Próximos a caducar: ', fg='blue').grid(row=2, column=3, pady=2)
        self.total_caducar = Label(frame3, text='', fg='brown')
        self.total_caducar.grid(row=2, column=4)

        # dentro de 15 a 18 dias
        Label(frame3, text='Dentro de 15 a 18 dias: ', fg='blue').grid(row=3, column=3, pady=2)
        self.total_caducar_15_18 = Label(frame3, text='', fg='brown')
        self.total_caducar_15_18.grid(row=4, column=3)
        # dentro de 8 a 11 dias
        Label(frame3, text='Dentro de 8 a 11 dias: ', fg='blue').grid(row=3, column=4, pady=2)
        self.total_caducar_8_11 = Label(frame3, text='', fg='brown')
        self.total_caducar_8_11.grid(row=4, column=4)
        # dentro de 1 a 4 dias
        Label(frame3, text='Dentro de 1 a 4 dias: ', fg='blue').grid(row=3, column=5, pady=2)
        self.total_caducar_1_4 = Label(frame3, text='', fg='brown')
        self.total_caducar_1_4.grid(row=4, column=5)
        # Button Actualizar Datos
        ttk.Button(frame3, text = 'ACTUALIZAR DATOS', command=self.actualizar_datos_generales).grid(row=5, column=4, padx=5, pady=5, sticky=W+E)



        # ====================== Frame contenedor 4 ======================================
        frame4 = LabelFrame(self.wind, text = 'Tabla de productos')
        frame4.grid(row=4, column=3, columnspan=6, pady=15)
        frame4.configure(font=("Arial", 12, "italic"))

        # Crear tabla
        self.tree = ttk.Treeview(frame4, height=12, columns=("#1", "#2", "#3", "#4", "#5"))
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.column("#0", width=120)
        self.tree.column("#1", width=100, anchor=CENTER)
        self.tree.column("#2", width=100, anchor=CENTER)
        self.tree.column("#3", width=100, anchor=CENTER)
        self.tree.column("#4", width=90, anchor=CENTER)
        self.tree.column("#5", width=90, anchor=CENTER)
        self.tree.heading('#0', text='Código', anchor=CENTER)
        self.tree.heading('#1', text='Marca', anchor=CENTER)
        self.tree.heading('#2', text='Nombre', anchor=CENTER)
        self.tree.heading('#3', text='Descripción', anchor=CENTER)
        self.tree.heading('#4', text='F. Creación', anchor=CENTER)
        self.tree.heading('#5', text='F. Vencimiento', anchor=CENTER)
        self.tree['selectmode']='browse' # para seleccionar un solo registro

        # Llenando las filas
        self.get_productos()

        # Scrollbar: barra de dezplazamiento
        sb = Scrollbar(frame4, orient=VERTICAL)
        sb.grid(row=5, column=2, sticky=N+S)
        self.tree.config(yscrollcommand=sb.set)
        sb.config(command=self.tree.yview)

        # Button Editar Eliminar 
        ttk.Button(frame4, text = 'EDITAR', command=self.editar_productos).grid(row=6, column=0, padx=5, pady=5, sticky=W+E)
        ttk.Button(frame4, text = 'ELIMINAR', command=self.eliminar_productos).grid(row=6, column=1, padx=5, pady=5, sticky=W+E)
        
        # Mensaje de salida 2
        self.mensaje2 = Label(frame4, text = '', fg='blue')
        self.mensaje2.grid(row=8, column=0, columnspan=3, sticky=W+E)


    def ventana_editar(self, codigo, marca, nombre, descripcion, f_vencimiento):

        self.editar_wind=Toplevel()  # Crea una ventana encima de la principal
        self.editar_wind.title = 'Editar Productos'
        
        self.codigo_editar = codigo
        Label(self.editar_wind, text='Código: ', fg='brown').grid(row=0, column=1, pady=10)
        Label(self.editar_wind, text=self.codigo_editar, fg='blue').grid(row=0, column=2, columnspan=2)
        
        Label(self.editar_wind, text='Marca: ',  fg='brown').grid(row=1, column=1, rowspan=2, pady=15)
        # Marca antiguo
        Label(self.editar_wind, text='Anterior: ').grid(row=1, column=2)
        Entry(self.editar_wind, textvariable=StringVar(self.editar_wind, value = marca), state='readonly').grid(row=1, column=3)
        # Marca nuevo
        Label(self.editar_wind, text='Nuevo: ').grid(row=2, column=2)
        self.nueva_marca = Entry(self.editar_wind)
        self.nueva_marca.grid(row=2, column=3)

        Label(self.editar_wind, text='Nombre: ',  fg='brown').grid(row=3, column=1, rowspan=2, pady=15)
        # Nombre antiguo
        Label(self.editar_wind, text='Anterior: ').grid(row=3, column=2)
        Entry(self.editar_wind, textvariable=StringVar(self.editar_wind, value = nombre), state='readonly').grid(row=3, column=3)
        # Nombre nuevo
        Label(self.editar_wind, text='Nuevo: ').grid(row=4, column=2)
        self.nuevo_nombre = Entry(self.editar_wind)
        self.nuevo_nombre.grid(row=4, column=3)

        Label(self.editar_wind, text='Descripción: ',  fg='brown').grid(row=5, column=1, rowspan=2, pady=15)
        # Descripcion antiguo
        Label(self.editar_wind, text='Anterior: ').grid(row=5, column=2)
        Entry(self.editar_wind, textvariable=StringVar(self.editar_wind, value = descripcion), state='readonly').grid(row=5, column=3)
        # Descripcion nuevo
        Label(self.editar_wind, text='Nuevo: ').grid(row=6, column=2)
        self.nueva_descripcion = Entry(self.editar_wind)
        self.nueva_descripcion.grid(row=6, column=3)

        # Fecha Actual
        Label(self.editar_wind, text='F. Creación: ', fg='brown').grid(row=7, column=1, pady=10)
        self.f_creacion = fechas.fecha_hoy_text()
        self.f_creacion_label = Label(self.editar_wind, text=self.f_creacion, fg='blue').grid(row=7, column=2, columnspan=2)

        Label(self.editar_wind, text='F. Vencimiento: ',  fg='brown').grid(row=8, column=1, rowspan=2, pady=15)
        # Fecha Vencimiento antiguo
        Label(self.editar_wind, text='Anterior: ').grid(row=8, column=2)
        Entry(self.editar_wind, textvariable=StringVar(self.editar_wind, value = f_vencimiento), state='readonly').grid(row=8, column=3)
        # Fecha Vencimiento nuevo
        Label(self.editar_wind, text='Nuevo: ').grid(row=9, column=2)
            # dia
        Label(self.editar_wind, text='Dia: ').grid(row=10, column=2, pady=2)
        self.nuevo_dia = Entry(self.editar_wind)
        self.nuevo_dia.grid(row=10, column=3)
            # mes
        Label(self.editar_wind, text='Mes: ').grid(row=11, column=2, pady=2)
        self.nuevo_mes = Entry(self.editar_wind)
        self.nuevo_mes.grid(row=11, column=3)
            # año
        Label(self.editar_wind, text='Año: ').grid(row=12, column=2, pady=2)
        self.nuevo_año = Entry(self.editar_wind)
        self.nuevo_año.grid(row=12, column=3)

        Button(self.editar_wind, text='Guardar cambios', command=self.ejcutar_edit).grid(row=13, column=2, pady=5, sticky=W+E)

        self.mensaje3 = Label(self.editar_wind, text = '', fg='blue')
        self.mensaje3.grid(row=14, column=1, columnspan=3, sticky=W+E)




    def limpiar_mensajes(self):
        self.mensaje['text'] = ''
        self.mensaje2['text'] = ''
        self.mensaje_user['text'] = ''

    def obtener_barcode(self):
        self.limpiar_mensajes() 
        if self.opcion_seleccionada.get() == 1:   
            self.codigo = barcode.lector_barcode(0)
            self.codigo_label['text'] = self.codigo
        elif self.opcion_seleccionada.get() == 2: 
            self.codigo = barcode.lector_barcode(1)
            self.codigo_label['text'] = self.codigo
        else:
            self.mensaje['text'] = 'Seleccione una cámara'
        
    def actualizar_datos_generales(self):
        self.limpiar_mensajes()
        productos_total = len(self.base_datos.leer_rows())
        caduca_15_18_dias = len(self.comparar.noti_15_18_dias())
        caduca_8_11_dias = len(self.comparar.noti_8_11_dias())
        caduca_1_4_dias = len(self.comparar.noti_8_11_dias())
        caduca_total = caduca_15_18_dias + caduca_8_11_dias + caduca_15_18_dias
        self.total_prod['text'] ='{}'.format(productos_total)
        self.total_caducar_15_18['text'] = '{}'.format(caduca_15_18_dias)
        self.total_caducar_8_11['text'] = '{}'.format(caduca_8_11_dias)
        self.total_caducar_1_4['text'] = '{}'.format(caduca_1_4_dias)
        self.total_caducar['text'] = '{}'.format(caduca_total)

    def get_productos(self):
        # limpiando la tabla
        records = self.tree.get_children()
        for elementos in records:
            self.tree.delete(elementos)

        # consultando los datos
        db_rows = self.base_datos.recorrer_rows()
        for row in db_rows:
            self.tree.insert('', 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))     
    
    def verificar_fecha_corecta(self, dia, mes, año):
        try:   
            vrf_dia = int(dia)
            vrf_mes = int(mes)
            vrf_año = int(año)
        except:
            return False 
        if vrf_dia<1 or vrf_dia>31:
            return False
        elif vrf_mes<1 or vrf_mes>12:
            return False
        elif vrf_año<2022 or len(str(vrf_año))!=4:
            return False
        else:
            return True

    def validacion_entry_completas(self, codigo, marca, nombre, descripcion, dia, mes, año):
        if codigo == '':
            a = False
        else:
            a = True
        b = len(marca)
        c = len(nombre)
        d = len(descripcion)
        e = len(dia)
        f = len(mes)
        g = len(año)
        return a and b != 0 and c != 0 and d != 0 and e != 0 and f != 0 and g != 0

    def limpiar_campos(self):
        self.codigo_label['text'] = ''
        self.marca.delete(0, END)
        self.nombre.delete(0, END)
        self.descripcion.delete(0, END)
        self.dia.delete(0, END)
        self.mes.delete(0, END)
        self.año.delete(0, END)

    def agregar_productos(self):
        self.limpiar_mensajes()
        try:
            codigo = self.codigo_label['text']
            marca = self.marca.get()
            nombre = self.nombre.get()
            descripcion = self.descripcion.get()
            dia = self.dia.get()
            mes = self.mes.get()
            año = self.año.get()
            confirmacion1 = self.validacion_entry_completas(codigo, marca, nombre, descripcion, dia, mes, año)
            confirmacion2 = self.verificar_fecha_corecta(dia, mes, año)  
            if confirmacion1 and confirmacion2:
                f_vencimiento = fechas.fecha_vencimiento(dia, mes, año)
                self.base_datos.insertar_producto(self.codigo,self.marca.get(),self.nombre.get(),self.descripcion.get(),self.f_creacion,f_vencimiento)
                self.mensaje['text']= 'Producto {} ha sido agregado'.format(self.nombre.get())
                self.limpiar_campos()
            elif not confirmacion1 and confirmacion2:
                self.mensaje['text']='Espacios incompletos'
            elif not confirmacion2 and confirmacion1:
                self.mensaje['text']='Fecha inadmisible'
            else:
                self.mensaje['text']='Rellene los campos'
        except:
            self.mensaje['text']='Verificar datos'
        self.get_productos()

    def editar_productos(self):
        selecionado = self.tree.focus()
        codigo = self.tree.item(selecionado, 'text')
        if codigo == '':
            self.mensaje2['text']='Debe seleccionar un registro'
        else:
            valores = self.tree.item(selecionado, 'values')
            marca = valores[0]
            nombre = valores[1]
            descripcion = valores[2]
            f_vencimiento = valores[4]
            self.ventana_editar(codigo, marca, nombre, descripcion, f_vencimiento)

    def ejcutar_edit(self):
        self.mensaje3['text'] = ''
        codigo = self.codigo_editar
        marca = self.nueva_marca.get()
        nombre = self.nuevo_nombre.get()
        descripcion = self.nueva_descripcion.get()
        dia = self.nuevo_dia.get()
        mes = self.nuevo_mes.get()
        año = self.nuevo_año.get()
        verificar1 = self.validacion_entry_completas(codigo, marca, nombre, descripcion, dia, mes, año)
        verificar2 = self.verificar_fecha_corecta(dia, mes, año)
        try:
            if verificar1 and verificar2:
                f_vencimiento = "{}/{}/{}".format(dia, mes, año)
                self.base_datos.actualizar_producto(codigo, marca, nombre, descripcion, f_vencimiento)
                self.editar_wind.destroy()
                self.mensaje2['text'] = 'Registro {} actualizado'.format(codigo)
                self.get_productos()  
            else:
                 self.mensaje3['text'] = "Verificar datos"
        except:
            self.mensaje3['text'] = "Verificar datos"

    def eliminar_productos(self):
        self.limpiar_mensajes()
        selecionado = self.tree.focus()
        codigo = self.tree.item(selecionado, 'text')
        if codigo == '':
            self.mensaje2['text']='Debe seleccionar un registro'
        else:
            valores = self.tree.item(selecionado, 'values')
            data ="{}, {}, {}".format(codigo, valores[0], valores[1])

            confirmacion = messagebox.askquestion("Eliminar", "¿Deseas eliminar el registro seleccionado?\n" + data)
            if confirmacion == messagebox.YES:
                self.base_datos.eliminar_producto(codigo)
                self.mensaje2['text']='{} eliminado correctamente'.format(data)
                self.get_productos()

    def alarmas(self):
        self.limpiar_mensajes()
        try:   
            destinatario = self.correo_user.get()
            nombre = self.nombre_user.get()
            
            # De 15 a 18 dias
            datos1 = self.comparar.noti_15_18_dias()
            if len(datos1) != 0: 
                self.g_mail.notificar_estado_producto(destinatario, nombre,  15, 18, datos1)

            # De 8 a 11 dias
            datos2 = self.comparar.noti_8_11_dias()
            if len(datos2) != 0: 
                self.g_mail.notificar_estado_producto(destinatario, nombre, 8, 11, datos2)
        
            # De 1 a 4 dias
            datos3 = self.comparar.noti_1_4_dias()
            if len(datos3) != 0: 
                self.g_mail.notificar_estado_producto(destinatario, nombre, 1, 4, datos3)
            # Excluyente 
            if len(datos1) == 0 and len(datos2) == 0 and len(datos3) == 0:
                self.g_mail.notificar_estado_producto(destinatario, nombre, 1, 19, datos3)
            self.mensaje_user['text'] = 'Se ha enviado estado de productos'
        except:
            self.mensaje_user['text'] = 'Verificar los datos ingresados'
        self.comparar.eliminar_vencidos()


if __name__ == '__main__':
    window = Tk() # crear ventana principal
    aplicacion = AppProductos(window)
    window.mainloop() # ejecutar ventana 