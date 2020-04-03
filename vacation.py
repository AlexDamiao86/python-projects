#Media de diaria em hoteis pesquisado de 140 reais

def hotel_cost(nights):
    return 140 * nights

"""Comentario de varias linhas
Valor medio de passagens aereas para determinadas cidades
Caso nao encontrado a cidade, será retornado Falso"""
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh": 
        return 222
    elif city == "Los Angeles":
        return 475
#Sem o else abaixo, caso nao encontrado a cidade, programa nao executarah
    else:
        return False


def rental_car_cost(days):
    car_cost = 40 * days
    if days >= 7:
        car_cost = car_cost - 50
    elif days >= 3:
        car_cost = car_cost - 20
    return car_cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("The trip cost is", trip_cost("Salvador", 5, 600))
