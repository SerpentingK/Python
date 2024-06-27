from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return "Calculador de pagos: Ingrese salario base, horas extras, 1 para bonificacion 2 para no bonificacion(no bonificacion por defecto.)"

@app.get("/{salario_base}/{horas_extras}/{r}")
def calcular_pago(salario_base:float, horas_extras:float, r:int):
    
    bonificacion = False
    if r == 1:
        bonificacion = True
    elif r == 2:
        bonificacion = False
        
    # Calcular el valor de una hora normal
    valor_hora_normal = salario_base / 192
    
    # Calcular el valor de las horas extras
    valor_hora_extra = valor_hora_normal * 1.25
    total_horas_extras = valor_hora_extra * horas_extras
    
    # Calcular bonificación
    if bonificacion:
        bonificacion_valor = salario_base * 0.05
    else:
        bonificacion_valor = 0.0
    
    # Calcular el salario total antes de descuentos
    salario_total_antes_descuentos = salario_base + total_horas_extras + bonificacion_valor
    
    # Calcular los descuentos
    descuento_salud = salario_total_antes_descuentos * 0.035
    descuento_pension = salario_total_antes_descuentos * 0.04
    descuento_caja_compensacion = salario_total_antes_descuentos * 0.01
    
    # Calcular el salario total después de descuentos
    salario_total_despues_descuentos = salario_total_antes_descuentos - (descuento_salud + descuento_pension + descuento_caja_compensacion)
    
    return {
        "salario_base": salario_base,
        "valor_hora_normal": valor_hora_normal,
        "total_horas_extras": total_horas_extras,
        "bonificacion": bonificacion_valor,
        "salario_total_antes_descuentos": salario_total_antes_descuentos,
        "descuento_salud": descuento_salud,
        "descuento_pension": descuento_pension,
        "descuento_caja_compensacion": descuento_caja_compensacion,
        "salario_total_despues_descuentos": round(salario_total_despues_descuentos, 2)
    }
