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


dict_units2meterpersecond_unit = {"Kilometer/Hour" : 0.2778,
                        "Meter/Second": 1,
                        "Mile/Hour": 0.44704
                        }
    
class converter:
    def __init__(self, in_unit, in_value, out_unit):
        self.in_unit = in_unit
        self.in_value = in_value
        self.out_unit = out_unit
           
    def in2grams(self,in_unit, in_value):
        return in_value * dict_units2grams_unit[in_unit]

    def grams2out(self,gms_value, out_unit):
        return gms_value / dict_units2grams_unit[out_unit]

    def mass_unit_converter(self,in_unit, in_value, out_unit):
        in_grams = self.in2grams(in_unit, in_value)
        return round(self.grams2out(in_grams, out_unit), 3)


    def in2meters(self,in_unit, in_value):
        return in_value * dict_units2meters_unit[in_unit]

    def meters2out(self,gms_value, out_unit):
        return gms_value / dict_units2meters_unit[out_unit]

    def distance_unit_converter(self,in_unit, in_value, out_unit):
        in_grams = self.in2meters(self,in_unit, in_value)
        return round(self.meters2out(self,in_grams, out_unit), 3)


    def in2meterspersecond(self,in_unit, in_value):
        return in_value * dict_units2meterpersecond_unit[in_unit]

    def meterspersecond2out(self,gms_value, out_unit):
        return gms_value / dict_units2meterpersecond_unit[out_unit]

    def speed_unit_converter(self,in_unit, in_value, out_unit):
        in_grams = self.in2meterspersecond(in_unit, in_value)
        return round(self.meterspersecond2out(in_grams, out_unit), 3)
        
    
    def cel2unit(self, in_value, out_unit):
        if out_unit == "Kelvin":
            return in_value + 273.15
        elif out_unit == "Fahrenheit":
            return (in_value*9/5)+32
    
    def kev2unit(self, in_value, out_unit):
        if out_unit == "Celcius":
            return in_value - 273.15
        elif out_unit == "Fahrenheit":
            return ((in_value-273.15)*9/5)+32
        
    def fahrenheit2unit(self, in_value, out_unit):
        if out_unit == "Celcius":
            return (in_value-32)*5/9
        elif out_unit == "Kelvin":
            return (in_value-32)*5/9+273.15
    
    def temp_unit_converter(self, in_unit, in_value, out_unit):
        if in_unit == "Celcius":
            x = round(self.cel2unit(in_value, out_unit),3)
        elif in_unit == "Kelvin":
            x = round(self.kev2unit(in_value, out_unit),3)
        elif in_unit == "Fahrenheit":
            x = round(self.fahrenheit2unit(in_value, out_unit),3)
        return x
    