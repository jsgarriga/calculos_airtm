# Calculadora de Tarifas de Airtm

Este repositorio contiene una serie de scripts de Python que te permiten calcular las tarifas de Airtm con diversas funciones. Estos scripts facilitan el cálculo de tarifas en pesos argentinos, manteniendo los valores actualizados a AirUSD y al dólar estadounidense. Construido con base en <https://help.airtm.com/es-LA/support/solutions/articles/47001186315--c%C3%B3mo-calcula-airtm-las-tarifas->.

## Descripción

Los scripts de este repositorio te permiten calcular las tarifas de Airtm para diferentes escenarios y transacciones. Cada script corresponde a una función específica que implementa una fórmula basada en las definiciones y ecuaciones del enlace anteriormente presentado.

Los principales scripts son:

- `calcular_fondos_por_recibir_agregar_p2p`: Calcula los fondos por recibir al agregar dinero P2P (mediante el envío de una solicitud).
- `calcular_fondos_a_enviar_agregar_p2p`: Calcula los fondos a enviar al agregar dinero P2P.
- `calcular_fondos_por_recibir_retirar_p2p`: Calcula los fondos por recibir al retirar dinero P2P (mediante el envío de una solicitud).
- `calcular_fondos_a_enviar_retirar_p2p`: Calcula los fondos a enviar al retirar dinero P2P.
- `calcular_fondos_por_recibir_agregar_banco_directo`: Calcula los fondos por recibir al agregar dinero con banco directo.
- `calcular_fondos_a_enviar_agregar_banco_directo`: Calcula los fondos a enviar al agregar dinero con banco directo.
- `calcular_fondos_por_recibir_retirar_banco_directo`: Calcula los fondos por recibir al retirar dinero con banco directo.
- `calcular_fondos_a_enviar_retirar_banco_directo`: Calcula los fondos a enviar al retirar dinero con banco directo.
- `calcular_fondos_por_recibir_retirar_criptomoneda_directa`: Calcula los fondos por recibir al retirar dinero de criptomoneda directa.
- `calcular_fondos_a_enviar_retirar_criptomoneda_directa`: Calcula los fondos a enviar al retirar dinero de criptomoneda directa.
- `calcular_fondos_por_recibir_agregar_tarjeta_debito_directo`: Calcula los fondos por recibir al agregar dinero con tarjeta de débito directo.
- `calcular_fondos_a_enviar_agregar_tarjeta_debito_directo`: Calcula los fondos a enviar al agregar dinero con tarjeta de débito directo.
- `calcular_fondos_por_recibir_aceptador_agregar`: Calcula los fondos por recibir del aceptador al agregar dinero como respuesta a una solicitud de retiro P2P.
- `calcular_fondos_a_enviar_aceptador_agregar`: Calcula los fondos a enviar del aceptador al agregar dinero como respuesta a una solicitud de retiro P2P.
- `calcular_fondos_por_recibir_aceptador_retirar`: Calcula los fondos por recibir del aceptador al retirar dinero como respuesta a una solicitud de retiro P2P.
- `calcular_fondos_a_enviar_aceptador_retirar`: Calcula los fondos a enviar del aceptador al retirar dinero como respuesta a una solicitud de retiro P2P.

## Uso

Ejemplo básico de cómo utilizar:

```python
from modules import calcs

fondos_a_enviar = 1000
tipo_cambio_mercado = 1.2
tarifa_deposito_garantia = 0.5
comision_fija_companero = 0.1
tarifa_servicio = 0.02
comision_variable_companero = 0.05

resultado = calcular_fondos_por_recibir_agregar_p2p(fondos_a_enviar, tipo_cambio_mercado, tarifa_deposito_garantia, comision_fija_companero, tarifa_servicio, comision_variable_companero)

print(resultado)
```