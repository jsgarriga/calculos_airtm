def calcular_fondos_por_recibir_agregar_p2p(fondos_a_enviar, tipo_cambio_mercado, tarifa_deposito_garantia, comision_fija_companero, tarifa_servicio, comision_variable_companero):
    """
    Calcula los fondos por recibir al agregar fondos mediante P2P (envío de solicitud).

    Args:
        fondos_a_enviar (float): Monto de fondos a enviar.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_deposito_garantia (float): Tarifa de depósito en garantía.
        comision_fija_companero (float): Comisión fija por compañero.
        tarifa_servicio (float): Tarifa de servicio.
        comision_variable_companero (float): Comisión variable por compañero.

    Returns:
        float: Fondos por recibir.
    """
    return (fondos_a_enviar / tipo_cambio_mercado - tarifa_deposito_garantia - comision_fija_companero) / (1 + tarifa_servicio + comision_variable_companero)


def calcular_fondos_a_enviar_agregar_p2p(fondos_por_recibir, tipo_cambio_mercado, tarifa_deposito_garantia, comision_fija_companero, tarifa_servicio, comision_variable_companero):
    """
    Calcula los fondos a enviar al agregar fondos mediante P2P (envío de solicitud).

    Args:
        fondos_por_recibir (float): Monto de fondos por recibir.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_deposito_garantia (float): Tarifa de depósito en garantía.
        comision_fija_companero (float): Comisión fija por compañero.
        tarifa_servicio (float): Tarifa de servicio.
        comision_variable_companero (float): Comisión variable por compañero.

    Returns:
        float: Fondos a enviar.
    """
    return (fondos_por_recibir * (1 + tarifa_servicio + comision_variable_companero) + tarifa_deposito_garantia + comision_fija_companero) * tipo_cambio_mercado


def calcular_fondos_por_recibir_retirar_p2p(fondos_a_enviar, tipo_cambio_mercado, tarifa_deposito_garantia, comision_fija_companero, tarifa_servicio, comision_variable_companero):
    """
    Calcula los fondos por recibir al retirar fondos mediante P2P (envío de solicitud).

    Args:
        fondos_a_enviar (float): Monto de fondos a enviar.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_deposito_garantia (float): Tarifa de depósito en garantía.
        comision_fija_companero (float): Comisión fija por compañero.
        tarifa_servicio (float): Tarifa de servicio.
        comision_variable_companero (float): Comisión variable por compañero.

    Returns:
        float: Fondos por recibir.
    """
    return ((fondos_a_enviar - tarifa_deposito_garantia - comision_fija_companero) * tipo_cambio_mercado) / (1 + tarifa_servicio + comision_variable_companero)


def calcular_fondos_a_enviar_retirar_p2p(fondos_por_recibir, tipo_cambio_mercado, tarifa_deposito_garantia, comision_fija_companero, tarifa_servicio, comision_variable_companero):
    """
    Calcula los fondos a enviar al retirar fondos mediante P2P (envío de solicitud).

    Args:
        fondos_por_recibir (float): Monto de fondos por recibir.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_deposito_garantia (float): Tarifa de depósito en garantía.
        comision_fija_companero (float): Comisión fija por compañero.
        tarifa_servicio (float): Tarifa de servicio.
        comision_variable_companero (float): Comisión variable por compañero.

    Returns:
        float: Fondos a enviar.
    """
    return ((fondos_por_recibir * (1 + tarifa_servicio + comision_variable_companero)) / tipo_cambio_mercado) + tarifa_deposito_garantia + comision_fija_companero


def calcular_fondos_por_recibir_agregar_banco_directo(fondos_a_enviar, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos por recibir al agregar fondos mediante banco directo.

    Args:
        fondos_a_enviar (float): Monto de fondos a enviar.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos por recibir.
    """
    return ((fondos_a_enviar / tipo_cambio_mercado) - tarifa_transferencia) / (1 + tarifa_servicio)


def calcular_fondos_a_enviar_agregar_banco_directo(fondos_por_recibir, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos a enviar al agregar fondos mediante banco directo.

    Args:
        fondos_por_recibir (float): Monto de fondos por recibir.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos a enviar.
    """
    return (fondos_por_recibir * (1 + tarifa_servicio) + tarifa_transferencia) * tipo_cambio_mercado


def calcular_fondos_por_recibir_retirar_banco_directo(fondos_a_enviar, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos por recibir al retirar fondos mediante banco directo.

    Args:
        fondos_a_enviar (float): Monto de fondos a enviar.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos por recibir.
    """
    return ((fondos_a_enviar - tarifa_transferencia) * tipo_cambio_mercado) / (1 + tarifa_servicio)


def calcular_fondos_a_enviar_retirar_banco_directo(fondos_por_recibir, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos a enviar al retirar fondos mediante banco directo.

    Args:
        fondos_por_recibir (float): Monto de fondos por recibir.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos a enviar.
    """
    return ((fondos_por_recibir * (1 + tarifa_servicio)) / tipo_cambio_mercado) + tarifa_transferencia


def calcular_fondos_por_recibir_retirar_criptomoneda_directa(fondos_a_enviar, tipo_cambio_mercado, blockchain_fee, tarifa_servicio):
    """
    Calcula los fondos por recibir al retirar fondos mediante criptomoneda directa.

    Args:
        fondos_a_enviar (float): Monto de fondos a enviar.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        blockchain_fee (float): Tarifa de la blockchain.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos por recibir.
    """
    return (fondos_a_enviar * tipo_cambio_mercado - blockchain_fee) / (1 + tarifa_servicio)


def calcular_fondos_a_enviar_retirar_criptomoneda_directa(fondos_por_recibir, tipo_cambio_mercado, tarifa_blockchain, tarifa_servicio):
    """
    Calcula los fondos a enviar al retirar fondos mediante criptomoneda directa.

    Args:
        fondos_por_recibir (float): Monto de fondos por recibir.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_blockchain (float): Tarifa de la blockchain.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos a enviar.
    """
    return ((fondos_por_recibir * (1 + tarifa_servicio)) / tipo_cambio_mercado) + tarifa_blockchain


def calcular_fondos_por_recibir_agregar_tarjeta_debito_directo(fondos_a_enviar, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos por recibir al agregar fondos mediante tarjeta de débito directo.

    Args:
        fondos_a_enviar (float): Monto de fondos a enviar.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos por recibir.
    """
    return ((fondos_a_enviar / tipo_cambio_mercado) - tarifa_transferencia) / (1 + tarifa_servicio)


def calcular_fondos_a_enviar_agregar_tarjeta_debito_directo(fondos_por_recibir, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos a enviar al agregar fondos mediante tarjeta de débito directo.

    Args:
        fondos_por_recibir (float): Monto de fondos por recibir.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos a enviar.
    """
    return (fondos_por_recibir * (1 + tarifa_servicio) + tarifa_transferencia) * tipo_cambio_mercado


def calcular_fondos_por_recibir_retirar_tarjeta_debito_directo(fondos_a_enviar, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos por recibir al retirar fondos mediante tarjeta de débito directo.

    Args:
        fondos_a_enviar (float): Monto de fondos a enviar.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos por recibir.
    """
    return ((fondos_a_enviar - tarifa_transferencia) * tipo_cambio_mercado) / (1 + tarifa_servicio)


def calcular_fondos_a_enviar_retirar_tarjeta_debito_directo(fondos_por_recibir, tipo_cambio_mercado, tarifa_transferencia, tarifa_servicio):
    """
    Calcula los fondos a enviar al retirar fondos mediante tarjeta de débito directo.

    Args:
        fondos_por_recibir (float): Monto de fondos por recibir.
        tipo_cambio_mercado (float): Tipo de cambio de mercado.
        tarifa_transferencia (float): Tarifa de transferencia.
        tarifa_servicio (float): Tarifa de servicio.

    Returns:
        float: Fondos a enviar.
    """
    return ((fondos_por_recibir * (1 + tarifa_servicio)) / tipo_cambio_mercado) + tarifa_transferencia

