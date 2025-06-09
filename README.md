# Integración API de Pagos Khipu (DemoBank)

Este proyecto muestra una integración simple y funcional con la API de pagos de Khipu, usando el entorno de pruebas DemoBank para simular cobros en pesos chilenos (CLP).

## Objetivo

El propósito de este proyecto es demostrar el proceso de creación de un enlace de pago utilizando la API de Khipu en modo desarrollador, sin crear cobros manuales desde el portal, sino realizando todo mediante llamadas a la API.

## Funcionalidades

- Generación automática del enlace de pago con datos de prueba (correo y monto).
- Enlace directo para completar el pago en el entorno simulado DemoBank.

## Instrucciones para probar

1. Clona el repositorio.
2. Ejecuta el script `khipu_api.py`.
3. El script generará el enlace de pago con datos fijos de prueba (correo y monto).
4. Puedes modificar esos datos directamente en el script para probar con otros valores.
5. Abre el enlace generado en tu navegador para simular la transacción en el entorno DemoBank.

## Capturas de pantalla

Se incluyen imágenes que muestran:

- Generación de enlace para pago.
- Selección de Banco (Demobank) para pagar.
- Selección de cuenta en DemoBank.
- Confirmación de transferencia.
- Visualización del pago realizado en el portal de desarrollador de Khipu.

## Consideraciones

Este proyecto utiliza la API en modo desarrollador y el entorno DemoBank, por lo que los pagos no son reales, sino simulados para fines de integración y prueba.

## Bibliografía

- [Documentación oficial de la API de pagos de Khipu](https://khipu.com/page/api)  
  Fuente principal utilizada para comprender el funcionamiento de la API, sus endpoints y ejemplos de integración en modo desarrollador.
