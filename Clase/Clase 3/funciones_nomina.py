def calcular_valor_dia(salario_basico):
    return round(salario_basico / 30, 2)

def calcular_valor_hora_basica(valor_dia):
    return round(valor_dia / 8, 2)

def calcular_valor_hora_extra_diurna(valor_hora_basica):
    return round(valor_hora_basica + (valor_hora_basica * 0.25), 2)

def calcular_valor_hora_extra_nocturna(valor_hora_basica):
    return round(valor_hora_basica + (valor_hora_basica * 0.35), 2)

def calcular_valor_hora_extra_festiva(valor_hora_basica):
    return round(valor_hora_basica + (valor_hora_basica * 0.75), 2)

def calcular_valor_hora_extra_dominical(valor_hora_basica):
    return round(valor_hora_basica * 2, 2)

def calcular_total_horas_extras(HorasExD, HorasExN, HorasExDom, HorasExF, valorHorasExD, valorHorasExN, valorHorasExDom, valorHorasExF):
    return (HorasExD * valorHorasExD) + (HorasExN * valorHorasExN) + (HorasExDom * valorHorasExDom) + (HorasExF * valorHorasExF)

def calcular_descuento_dias_no_laborados(dias_no_lab, valor_dia):
    return dias_no_lab * valor_dia

def calcular_salario_total(salario_basico, descuento_dias_no_laborados, total_horas_extras):
    return round(salario_basico - descuento_dias_no_laborados + total_horas_extras, 2)
