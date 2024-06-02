dict_units2grams_unit = {"Picogram": 0.000000000001,
                    "Nanogram": 0.000000001,
                    "Microgram": 0.000001,
                    "Milligram": 0.001,
                    "Centigram": 0.01,
                    "Decigram": 0.1,
                    "Gram": 1,
                    "Dekagram": 10,
                    "Hectogram": 100,
                    "Kilogram": 1000,
                    "Tonne": 1000_000,
                    "Kilotonne": 1000_000_000,
                    "Megatonne": 1000_000_000_000,
                    "Gigatonne": 1000_000_000_000_000,
                    
                    "Pound" : 453.592,
                    "Ounce" : 28.3495,
                    "Stone": 6350.29,
                    "US Ton": 907185
                    }

dict_units2meters_unit = {"Picometer": 0.000000000001,
                    "Nanometer": 0.000000001,
                    "Micrometer": 0.000001,
                    "Millimeter": 0.001,
                    "Centimeter": 0.01,
                    "Decimeter": 0.1,
                    "Meter": 1,
                    "Dekameter": 10,
                    "Hectometer": 100,
                    "Kilometer": 1000,
                    "Mile":1609.34,
                    "Inch": 0.0254,
                    "Yard": 0.9144, 
                    "Foot": 0.3048,
                    "Rod": 5.0292
                    }



def in2grams(in_unit, in_value):
    return in_value * dict_units2grams_unit[in_unit]

def grams2out(gms_value, out_unit):
    return gms_value / dict_units2grams_unit[out_unit]

def mass_unit_converter(in_unit, in_value, out_unit):
    in_grams = in2grams(in_unit, in_value)
    return round(grams2out(in_grams, out_unit), 3)



def in2meters(in_unit, in_value):
    return in_value * dict_units2meters_unit[in_unit]

def meters2out(gms_value, out_unit):
    return gms_value / dict_units2meters_unit[out_unit]

def distance_unit_converter(in_unit, in_value, out_unit):
    in_grams = in2meters(in_unit, in_value)
    return round(meters2out(in_grams, out_unit), 3)


    
