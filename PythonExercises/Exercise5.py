#Exercise 5

def convert_temp():
    f = int(input("Enter a temperature in Fahrenheit: "))
    print("The temperature in Celsius: ",convert_to_celsius(f))
    print("The temperature in Kelvin is: ", convert_to_kelvin(convert_to_celsius(f)))


def convert_to_celsius(fahrenheit):
    celsius = (5/9)*(fahrenheit-32)
    return celsius

def convert_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

convert_temp()
    
