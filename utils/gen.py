from datetime import datetime
def validate_date_in(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validar_rut(rut_numero, rut_dv):
    rut_numero = rut_numero.replace(".", "")
    if len(rut_numero) != 8:
        return False
    suma = 0
    multiplicador = 2
    for i in reversed(rut_numero):
        suma += int(i) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2
    resto = suma % 11
    dv_esperado = 11 - resto if resto != 0 else 0
    if str(dv_esperado) == rut_dv or (rut_dv.upper() == 'K' and dv_esperado == 10):
        return True
    else:
        return False