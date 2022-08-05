import cv2
from pyzbar import pyzbar

def lector_barcode():
    # Encendemos la camara con OpenCV
    cap = cv2.VideoCapture(1)
    # Verificamos que la camara este encendida
    if not cap.isOpened():
        print("Error")
    while cap.isOpened():
        ret, frame = cap.read() # frame: obtendra el fotograma de la camara, ret: booleano
        if ret:
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                # Dibujar rectangulo
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type
                # Dibujar una cadena de texto
                text = "{} ({})".format(barcode_data, barcode_type)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
                print("[INFO] Found {} barcode: {}".format(barcode_type, barcode_data))
            # Muestra la imagen es una ventana especificada.
            cv2.imshow('Leer codigo de barras', frame)
            # Presionar Esc para cerrar
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break
        # Cierra el dispositivo de captura.
    cap.release()
    cv2.destroyAllWindows() 
    
    return barcode_data 


if __name__ == "__main__":
    print(lector_barcode())