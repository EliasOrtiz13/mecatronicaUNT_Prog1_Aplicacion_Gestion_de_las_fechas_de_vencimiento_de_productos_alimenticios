import conexion_sqlite3 as sql
import fechas

class Comparar():

    def __init__(self):
        self.sql = sql.Comunicacion()
        self.datos = self.sql.leer_rows()

    def noti_15_18_dias(self):
        lst_15_18_dias = []
        
        for i in range(len(self.datos)):
            fecha_vencimiento = self.datos[i][5]
            resta = fechas.resta_fecha_post_actual(fecha_vencimiento)
            
            if resta <= 18 and resta >= 15:
                lst_15_18_dias.append(self.datos[i])

        return lst_15_18_dias


    def noti_8_11_dias(self):
        lst_8_11_dias = []
        
        for i in range(len(self.datos)):
            fecha_vencimiento = self.datos[i][5]
            resta = fechas.resta_fecha_post_actual(fecha_vencimiento)
            
            if resta <= 11 and resta >= 8:
                lst_8_11_dias.append(self.datos[i])
        
        return lst_8_11_dias


    def noti_1_4_dias(self):
        lst_1_4_dias = []

        for i in range(len(self.datos)):
            fecha_vencimiento = self.datos[i][5]
            resta = fechas.resta_fecha_post_actual(fecha_vencimiento)

            if resta <= 4 and resta >= 1:
                lst_1_4_dias.append(self.datos[i])

        return lst_1_4_dias


    def eliminar_vencidos(self):

        for i in range(len(self.datos)):
            fecha_vencimiento = self.datos[i][5]
            resta = fechas.resta_fecha_post_actual(fecha_vencimiento)

            if resta <= -2:
                self.sql.eliminar_producto(self.datos[i][0])

if __name__ == "__main__":
    alarma = Comparar()
    alarma.noti_1_4_dias()