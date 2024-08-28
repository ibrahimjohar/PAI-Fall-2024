#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 01

def area_trapezoid(s1, s2, h):
    return ((s1+s2)*h)/2
    
def area_parallelogram(b, h):
    return (b*h)

def volume_cylinder(r, h):
    return ((3.142)*(r*r)*h)

def surfacearea_cylinder(r, h):
    return ((2*(3.142)*r*h)+(2*(3.142)*(r*r)))

print("welcome to area/volume/surface area program.")

print("\n1. area of a trapezoid\n2. area of a parallelogram\n3. surface area of a cylinder\n4. volume of a cylinder\n")

choice = str(input("choose option num, you would like to calculate: "))

if (choice == '1'):
    print("area of trapezoid selected:\nenter information:")
    s1 = float(input("side 1: "))
    s2 = float(input("side 2: "))
    h = float(input("height: "))
    print("area - trapezoid = ", area_trapezoid(s1, s2, h))
elif (choice == '2'):
    print("area of parallelogram selected:\nenter information:")
    b = float(input("base: "))
    h = float(input("height: "))
    print("area - parallelogram = ", area_parallelogram(b, h))
elif (choice == '3'):
    print("surface area of cylinder selected:\nenter information:")
    r = float(input("radius: "))
    h = float(input("height: "))
    print("volume - cylinder = ", surfacearea_cylinder(r, h))
elif (choice == '4'):
    print("volume of cylinder selected:\nenter information:")
    r = float(input("radius: "))
    h = float(input("height: "))
    print("volume - cylinder = ", volume_cylinder(r, h))
