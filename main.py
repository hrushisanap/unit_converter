from unit_converter_class import converter as ucc


def main():
    temp_var = input(("""What do you want to convert?\nDistance | Mass | Speed| Temperature\n""")).title()
    
    if temp_var == "Weight" or temp_var == "Mass":
        print(mass_converter())
        
    elif temp_var == "Distance":
        print(distance_converter())
        
    elif temp_var == "Velocity" or temp_var == "Speed":
        print(speed_converter())
        
    elif temp_var == "Temperature":
        print(temp_converter())
        

def mass_converter():
    print("""Choose from following units:
    Picogram | Nanogram | Microgram | Milligram | Centigram | Decigram |
    Gram | Dekagram | Hectogram | Kilogram | Tonne | Kilotonne |
    Megatonne | Gigatonne | Pound | Ounce | Stone | US Ton \n""")

    mass_in_unit = input("you want to convert from: ").title()
    mass_in_value = float(input(f"value of {mass_in_unit}s: "))
    mass_out_unit = input("you want to convert to: ").title()
    
    mass = ucc(mass_in_unit, mass_in_value, mass_out_unit)
    return mass.mass_unit_converter(mass_in_unit, mass_in_value, mass_out_unit)
    
    
def distance_converter():
    print("""Choose from following units:
     "Picometer | Nanometer | Micrometer | Millimeter | Centimeter | 
     Decimeter | Meter | Dekameter | Hectometer | Kilometer | Mile | 
     Inch | Yard | Foot | Rod\n""")

    distance_in_unit = input("you want to convert from: ").title()
    distance_in_value = float(input(f"value of {distance_in_unit}s: "))
    distance_out_unit = input("you want to convert to: ").title()
    
    distance = ucc(distance_in_unit, distance_in_value, distance_out_unit)
    return distance.distance_unit_converter(distance_in_unit, distance_in_value, distance_out_unit)


def speed_converter():
    print("""Choose from following units:
    Meter/Second | Kilometer/Hour | Mile/Hour\n""")

    speed_in_unit = input("you want to convert from: ").title()
    speed_in_value = float(input(f"value of {speed_in_unit}s: "))
    speed_out_unit = input("you want to convert to: ").title()
    
    speed = ucc(speed_in_unit, speed_in_value, speed_out_unit)
    return speed.speed_unit_converter(speed_in_unit, speed_in_value, speed_out_unit)


def temp_converter():
    print("""Choose from following units:
    Celsius | Kelvin | Fahrenheit\n""")

    temp_in_unit = input("you want to convert from: ").title()
    temp_in_value = float(input(f"value of {temp_in_unit}s: "))
    temp_out_unit = input("you want to convert to: ").title()
    
    temp = ucc(temp_in_unit, temp_in_value, temp_out_unit)
    return temp.temp_unit_converter(temp_in_unit, temp_in_value, temp_out_unit)


if __name__ == "__main__":
    main()