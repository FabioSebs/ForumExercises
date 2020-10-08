#Exercise 2

def calc_weight_on_planet(weight , gravity=23.1):
    mass = weight/9.8
    new_weight = mass*gravity
    return str(new_weight)

print(calc_weight_on_planet(120,9.80)+"\n"+calc_weight_on_planet(120)+"\n"+calc_weight_on_planet(120, 23.1))

