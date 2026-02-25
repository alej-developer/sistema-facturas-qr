import qrcode
import json

# Este es el JSON que representa los datos de nuestra factura
datos_factura = {
    "id_factura": "F-2023-0045",
    "fecha": "2023-10-27",
    "proveedor": "Restaurante Sopa de Caracol",
    "conceptos": [
        {"descripcion": "Menú del día", "cantidad": 2, "precio_unitario": 15.00},
        {"descripcion": "Tapa de queso", "cantidad": 1, "precio_unitario": 4.00},
        {"descripcion": "Cerveza", "cantidad": 3, "precio_unitario": 2.50}
    ],
    "impuestos_porcentaje": 10,
    "total_pagado": 49.50
}

# Convertimos el diccionario de Python a un texto JSON estructurado
texto_json = json.dumps(datos_factura)

# Generamos el código QR con el texto JSON dentro
imagen_qr = qrcode.make(texto_json)
imagen_qr.save("factura_prueba.png")
               
print("Código QR generado exitosamente como 'factura_prueba.png'")