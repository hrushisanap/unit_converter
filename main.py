import unit_converter_class as ucc


print("""Choose from following units:
    Picogram | Nanogram | Microgram | Milligram | Centigram | Decigram |
    Gram | Dekagram | Hectogram | Kilogram | Tonne | Kilotonne |
    Megatonne | Gigatonne | Pound | Ounce | Stone | US Ton \n""")

mass_in_unit = input("you want to convert from: ").title()
mass_in_value = float(input(f"value of {mass_in_unit}s: "))
mass_out_unit = input("you want to convert to: ").title()

x = ucc.mass_unit_converter(mass_in_unit, mass_in_value, mass_out_unit)
print(x)