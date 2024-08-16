def calcular_nomina(sueldo, dias_trabajados, horas_trabajadas, comisiones, horas_extras):
    if sueldo <= 0:
        raise ValueError("El sueldo debe ser mayor que 0")
    if dias_trabajados <= 0 or dias_trabajados > 30:
        raise ValueError("Los días trabajados deben estar entre 1 y 30")
    if horas_trabajadas < 0 or horas_trabajadas > 24:
        raise ValueError("Las horas trabajadas deben estar entre 0 y 24")
    if comisiones < 0:
        raise ValueError("Las comisiones no pueden ser negativas")
    if horas_extras < 0:
        raise ValueError("Las horas extras no pueden ser negativas")

    # Cálculo de la nómina base
    pago_dia = sueldo / 30
    pago_horas = sueldo / 240  # Valor por hora
    pago_horas_extras = pago_horas * horas_extras * 1.25  # Horas extras con 25% adicional
    
    # Total devengado considerando el sueldo base, horas trabajadas, y comisiones
    total_devengado = (pago_dia * dias_trabajados) + comisiones + pago_horas_extras
    
    # Deducciones de salud (4%) y pensión (4%)
    deducciones_salud = total_devengado * 0.04
    deducciones_pension = total_devengado * 0.04
    
    total_deducido = deducciones_salud + deducciones_pension
    
    nomina_final = total_devengado - total_deducido
    
    return {
        "total_devengado": total_devengado,
        "deducciones_salud": deducciones_salud,
        "deducciones_pension": deducciones_pension,
        "total_deducido": total_deducido,
        "nomina_final": nomina_final
    }
