def rental_car_cost(d):
    cost = 40
    total = d * cost
    
    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20
    return total
        
print(rental_car_cost(7))