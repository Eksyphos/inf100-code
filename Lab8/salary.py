
def weekly_pay(hourly_rate,hours):
    if hourly_rate<200:
        return 'Minstelønnskravet er ikke oppfylt'
    elif hours>60:
        return 'En ansatt jobber mer enn 60 timer'
    
    
    if hours>40:
        overtime = hours-40
        pay = hourly_rate*40 + overtime*(hourly_rate*1.5)
        return pay
    return hourly_rate*hours
