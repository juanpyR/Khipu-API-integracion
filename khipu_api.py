import requests
import webbrowser
import re
import time
import random

def correo_valido(correo):
    """
    Valida que el correo tenga un formato correcto usando expresión regular.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Patrón básico para correo
    return re.match(patron, correo)

def generar_transaction_id():
    """
    Genera un ID único para la transacción.
    Combina el timestamp actual en milisegundos con un número aleatorio de 5 dígitos.
    Esto ayuda a que cada ID sea distinto para evitar repeticiones.
    """
    timestamp = int(time.time() * 1000)  # Tiempo actual en milisegundos
    random_part = random.randint(10000, 99999)  # Número aleatorio de 5 dígitos
    return f"tx{timestamp}{random_part}"

def crear_pago_khipu(correo, monto, descripcion):
    """
    Realiza la solicitud a la API de Khipu para crear un pago.
    Envía la información necesaria y recibe el enlace para pagar.
    Retorna el enlace directo y el ID de transacción si todo sale bien.
    """
    url = "https://payment-api.khipu.com/v3/payments"
    headers = {
        "x-api-key": "d32b1ff1-bed5-4a0d-8c52-997935f1ed5c",
        "Content-Type": "application/json"
    }

    transaction_id = generar_transaction_id()  # Generar ID único
    moneda = "CLP"  # Moneda para mercado chileno

    # Preparar datos para enviar a la API
    payload = {
        "amount": monto,
        "currency": moneda,
        "subject": "Pago por compra de producto",
        "payer_email": correo,
        "transaction_id": transaction_id,
        "return_url": "https://www.khipu.com/en-us/",
        "cancel_url": "https://www.khipu.com/en-us/",
        "notify_url": "https://www.khipu.com/en-us/"
    }

    # Enviar petición POST a la API de Khipu
    response = requests.post(url, json=payload, headers=headers)

    # Verificar si la respuesta fue exitosa
    if response.status_code == 200:
        payment = response.json()
        enlace_directo = payment.get("simplified_transfer_url")
        if enlace_directo:
            enlace_directo += "?fallback=false"  # Formato directo para entrar al banco
            return enlace_directo, transaction_id
        else:
            print("No se recibió el enlace de pago esperado.")
            return None, None
    else:
        # Mostrar error si no fue exitosa la petición
        print(f"Error {response.status_code} al crear el pago:")
        print(response.text)
        return None, None

def iniciar_flujo_pago():
    print("\nGenerador de pago Khipu")

    # Solicitar monto válido
    while True:
        entrada = input("Monto a pagar en CLP: ").strip()
        if entrada.lower() == "cancelar":
            print("Operación cancelada.")
            return
        try:
            monto = int(entrada)
            if monto > 0:
                break
            print("El monto debe ser mayor a cero.")
        except ValueError:
            print("Por favor ingresa un número válido.")

    # Solicitar correo válido
    while True:
        correo = input("Correo del pagador: ").strip()
        if correo.lower() == "cancelar":
            print("Operación cancelada.")
            return
        if correo_valido(correo):
            break
        print("Correo no tiene un formato válido.")

    # Se pide la descripción pero se puede dejar en vacío ya que se asigna por defecto
    descripcion = input("Motivo del pago (puede dejar vacío): ").strip()
    if not descripcion:
        descripcion = "Pago por compra de producto"

    print("\nGenerando enlace de pago...")

    enlace, tx_id = crear_pago_khipu(correo, monto, descripcion)

    if enlace:
        print("\nPago creado con éxito.")
        print(f"Link de pago: {enlace}")
        print(f"ID de transacción: {tx_id}")
        webbrowser.open(enlace)
        print("Se abrió el navegador para completar el pago.")
    else:
        print("No se pudo generar el pago.")

# Activación del script de pago
if __name__ == "__main__":
    iniciar_flujo_pago()
