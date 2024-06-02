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


def in2grams(in_unit, in_value):
    return in_value * dict_units2grams_unit[in_unit]

def grams2out(gms_value, out_unit):
    return gms_value / dict_units2grams_unit[out_unit]


def mass_unit_converter(in_unit, in_value, out_unit):
    in_grams = in2grams(in_unit, in_value)
    return round(grams2out(in_grams, out_unit), 3)



    
