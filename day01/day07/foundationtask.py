def fahrenheit_to_celsius():
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"{f}°F is {round(c, 1)}°C")
    
fahrenheit_to_celsius()