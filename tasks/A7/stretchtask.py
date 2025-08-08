def rectangle_calculator():
    print("Rectangle Calculator")
    length = float(input("Length: "))
    width = float(input("Width: "))
    
    perimeter = 2 * (length + width)
    area = length * width
    
    print(f"Perimeter: {int(perimeter)}")
    print(f"Area: {int(area)}")
    
rectangle_calculator()