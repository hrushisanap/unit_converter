import unit_converter_class as ucc


def main():
    temp_var = input(("""What do you want to convert?\nDistance | Mass | Speed\n""")).title()
    
    if temp_var == "Weight" or temp_var == "Mass":
        print(mass_converter())
        
    if temp_var == "Distance":
        print(distance_converter())
        
    if temp_var == "Velocity" or temp_var == "Speed":
        speed_converter()
        

def mass_converter():
    print("""Choose from following units:
    Picogram | Nanogram | Microgram | Milligram | Centigram | Decigram |
    Gram | Dekagram | Hectogram | Kilogram | Tonne | Kilotonne |
    Megatonne | Gigatonne | Pound | Ounce | Stone | US Ton \n""")

    mass_in_unit = input("you want to convert from: ").title()
    mass_in_value = float(input(f"value of {mass_in_unit}s: "))
    mass_out_unit = input("you want to convert to: ").title()

    return ucc.mass_unit_converter(mass_in_unit, mass_in_value, mass_out_unit)
    
    
def distance_converter():
    print("""Choose from following units:
     "Picometer | Nanometer | Micrometer | Millimeter | Centimeter | 
     Decimeter | Meter | Dekameter | Hectometer | Kilometer | Mile | 
     Inch | Yard | Foot | Rod\n""")

    distance_in_unit = input("you want to convert from: ").title()
    distance_in_value = float(input(f"value of {distance_in_unit}s: "))
    distance_out_unit = input("you want to convert to: ").title()

    return ucc.distance_unit_converter(distance_in_unit, distance_in_value, distance_out_unit)


def speed_converter():
    pass


if __name__ == "__main__":
    main()