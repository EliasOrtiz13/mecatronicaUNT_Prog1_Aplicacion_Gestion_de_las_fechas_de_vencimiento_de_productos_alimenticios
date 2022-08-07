import datetime

def fecha_hoy_text():
    ahora = datetime.datetime.now()
    hoy_text = ahora.strftime('%d/%m/%Y')
    return hoy_text
# =========================

def formato_fecha_text(dia, mes, año):
    fecha = datetime.datetime(año, mes, dia)
    fecha_text = fecha.strftime('%d/%m/%Y')
    return fecha_text
# =========================

# fecha_post como cadena
def resta_fecha_post_actual(fecha_post):
    end_date = datetime.datetime.strptime(fecha_post, '%d/%m/%Y')
    diff = end_date - datetime.datetime.now()
    return diff.days
# =========================

def resta_fechas(fecha1, fecha2):
    start_date = datetime.datetime.strptime(fecha1, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(fecha2, '%d/%m/%Y')
    diff = end_date - start_date
    return diff.days


if __name__ == '__main__':
    # print(resta_fechas('10/09/2018', '10/09/2018'))
    # print(resta_fechas('10/09/2018', '20/09/2018'))
    print(type(formato_fecha_text()))
    print(formato_fecha_text())