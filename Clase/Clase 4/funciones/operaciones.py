def salario_horas_extras(sb, nhed, nhen, nhef, nhedo):
    vhed = (sb/240 * 1.25) * nhed
    vhen = (sb/240 * 1.35) * nhen
    vhef = (sb/240 * 1.75) * nhef
    vhedo = (sb/240 * 2) * nhedo
    
    return sb + vhed + vhen + vhef + vhef + vhedo

def descuento_dias_no_trabajados(sb, ndnt):
    return sb/30 + ndnt

def seguridad_social(ti):
    ss = ti * 0.08
    return ss
    
