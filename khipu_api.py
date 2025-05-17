import requests


def generar_enlace_pago(correo, monto):
     # URL de la API de Khipu para crear un pago
    url = "https://payment-api.khipu.com/v3/payments"

    # Headers con la clave API y el tipo de contenido JSON
    headers = {
        "x-api-key":"d32b1ff1-bed5-4a0d-8c52-997935f1ed5c" ,
        "Content-Type" : "application/json"
    }

    # Datos que se envían en el payload para crear el pago
    payload = {
        "subject": "Pagó por la compra del producto",
        "currency": "CLP",
        "amount": monto,
        "payer_email": correo
    }
    # Realiza la solicitud POST a la API para crear el pago
    response = requests.post(url, json=payload, headers=headers)

    # Si la respuesta es exitosa (código 200)
    if response.status_code == 200:
        payment = response.json() # Convierte la respuesta JSON en diccionario
        enlace_directo = payment["simplified_transfer_url"] + "?fallback=false"
        return enlace_directo
    else:

        # Si hubo un error, muestra el código y mensaje de error
        print(f"Error {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    # Datos de prueba: monto y correo electrónico
    monto = 4000
    correo = "prueba@gmail.com"

    # Genera el enlace de pago con los datos indicados
    enlace_pago = generar_enlace_pago(correo, monto)
    if enlace_pago:
        print(f"\n El monto a transferir es: {monto}")
        print(f"\n El Email para enviar el comprobante es: {correo}")
        print(f"\n Enlace directo al banco:\n{enlace_pago}\n")

