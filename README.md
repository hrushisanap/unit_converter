# Unit Converter

This repository contains a Python application that can convert units of distance, mass, speed, and temperature. The application consists of two main files: `unit_converter_class.py` and `main.py`.

## Features

- **Mass Conversion**: Convert between different units of mass such as grams, kilograms, pounds, ounces, etc.
- **Distance Conversion**: Convert between different units of distance such as meters, kilometers, miles, inches, etc.
- **Speed Conversion**: Convert between different units of speed such as meters per second, kilometers per hour, and miles per hour.
- **Temperature Conversion**: Convert between Celsius, Kelvin, and Fahrenheit.

## File Descriptions

### `unit_converter_class.py`

This file contains the `converter` class, which includes methods for converting between different units. It includes the following conversion methods:

- **Mass Conversion**:
  - `in2grams`: Convert input unit to grams.
  - `grams2out`: Convert grams to the output unit.
  - `mass_unit_converter`: Main method for mass conversion.

- **Distance Conversion**:
  - `in2meters`: Convert input unit to meters.
  - `meters2out`: Convert meters to the output unit.
  - `distance_unit_converter`: Main method for distance conversion.

- **Speed Conversion**:
  - `in2meterspersecond`: Convert input unit to meters per second.
  - `meterspersecond2out`: Convert meters per second to the output unit.
  - `speed_unit_converter`: Main method for speed conversion.

- **Temperature Conversion**:
  - `cel2unit`: Convert Celsius to Kelvin or Fahrenheit.
  - `kev2unit`: Convert Kelvin to Celsius or Fahrenheit.
  - `fahrenheit2unit`: Convert Fahrenheit to Celsius or Kelvin.
  - `temp_unit_converter`: Main method for temperature conversion.

### `main.py`

This file contains the main function and the user interface for the application. It includes functions to handle user inputs and call the appropriate conversion methods from the `converter` class.

- **Main Function**:
  - `main`: Prompts the user to choose the type of conversion (mass, distance, speed, temperature) and calls the corresponding function.

- **Conversion Functions**:
  - `mass_converter`: Handles user inputs for mass conversion and calls the mass conversion method.
  - `distance_converter`: Handles user inputs for distance conversion and calls the distance conversion method.
  - `speed_converter`: Handles user inputs for speed conversion and calls the speed conversion method.
  - `temp_converter`: Handles user inputs for temperature conversion and calls the temperature conversion method.

## Usage

To use this application, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/unit_converter.git
    ```
2. Navigate to the project directory:
    ```sh
    cd unit_converter
    ```
3. Run the main program:
    ```sh
    python main.py
    ```

4. Follow the on-screen prompts to perform the desired conversion.

## Example

### Mass Conversion

```sh
What do you want to convert?
Distance | Mass | Speed| Temperature
Mass
Choose from following units:
Picogram | Nanogram | Microgram | Milligram | Centigram | Decigram |
Gram | Dekagram | Hectogram | Kilogram | Tonne | Kilotonne |
Megatonne | Gigatonne | Pound | Ounce | Stone | US Ton 

you want to convert from: Kilogram
value of Kilograms: 5
you want to convert to: Pound
```
Output:
```sh
11.023
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please contact me at hrushinstudy@gmail.com .