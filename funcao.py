import datetime

dia_de_nasc = datetime.date(day=28, year=1997, month=3)

calcular_dias_de_vida(dia_de_nasc)

def calcular_dias_de_vida(data):
    if data is None:
       error = 'ops'
       return error

    hoje = datetime.date.today
    dias_de_vida = hoje - data
    return dias_de_vida
