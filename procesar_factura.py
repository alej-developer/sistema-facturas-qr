import cv2
from pyzbar.pyzbar import decode
import json

def leer_qr(ruta_imagen):
    """Lee un código QR desde una imagen y devuelve el texto decodificado."""
    #Cargar la imagen usando OpenCV
    imagen = cv2.imread(ruta_imagen)

    if imagen is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return None
    
    # Decodificar códigos de barrar y QR en la imagen
    objetos_decodificados = decode(imagen)

    for objeto in objetos_decodificados:
        #El texto extraido viene en formato de bytes, lo decodificamos a string (UTF-8)
        texto_extraido = objeto.data.decode("utf-8")
        return texto_extraido
    
    return None

def analizar_factura(datos_factura): 
    """Realiza operaciones deductivas y validaciones sobre los datos de la factura."""
print("\n--- INICIANDO AUDITORÍA DE FACTURA ---\n" \
print(f"Proveedor: {datos_factura['proveedor']} | ID: {datos_factura['id_factura']}")

subtotal_calculado = 0 

print("\nDesglose de arttículos:")
for articulo in datos_factura["conceptos"]:
    costo_linea = articulo["cantidad"] * articulo["precio_unitario"]
    subtotal_calculado += costo_linea
    print(f" > {articulo['cantidad']}} x {articulo['descripcion']}: ") {costo_linea:.2f} EUR")

#Cálculos finales 
impuestos_calculados = subtotal_calculado * (datos_factura["impuestos_porcentaje"] / 100)
total_calculado = subtotal_calculado + impuestos_calculados

print("\n--- RESULTADOS DEL ANÁLISIS ---")
print(f"Total reportado en factura: {datos_factura['total_pagado']:.2f} EUR")
print(f"Total calculado por el sistema: {total_calculado:.2f} EUR")

#Validación lógica
if abs(datos_factura['total_pagado'] - total_calculado) < 0.01: # Margen para decimales
    print("✅ ESTADO: Válido. Los montos coinciden perfectamente")
else:
    print("⚠️ ESTADO: Alerta. Discrepancia matemática detectada en la factura.")
    
# --- FLUJO PRINCIPAL DEL PROGRAMA --- 
if __name__ == "__main__":
    archivo_imagen = "factura_prueba.png"
    print(f"Escaneando documento: {archivo_imagen}...")

    texto_qr = leer_qr(archivo_imagen)

    if texto_qr:
        print("\nLectura exitosa. Transformando JSON A estructura Python...")
        try: 
            # Traducir el texto JSON a un Diccionario
            factura_dict = json.loads(texto_qr)

            # Ejecutar operaciones con los datos
            analizar_factura(factura_dict)

        except json.JSONDecodeError:
            print("Error: El contenido del QR no es un JSON válido.")

        else: 
            print("No se detectó ningún código QR en la imagen aportada.")
            

