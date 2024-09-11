def convert_units(input_str):
    # Splitting input into number and unit
    parts = input_str.split()
    value = float(parts[0])
    unit = parts[1]

    # Conversion factors
    if unit == "cm":
        converted_value = value / 2.54
        target_unit = "in"
    elif unit == "in":
        converted_value = value * 2.54
        target_unit = "cm"
    elif unit == "yd":
        converted_value = value * 0.9144
        target_unit = "m"
    elif unit == "m":
        converted_value = value / 0.9144
        target_unit = "yd"
    elif unit == "oz":
        converted_value = value * 28.349523125
        target_unit = "g"
    elif unit == "g":
        converted_value = value / 28.349523125
        target_unit = "oz"
    elif unit == "lb":
        converted_value = value * 0.45359237
        target_unit = "kg"
    elif unit == "kg":
        converted_value = value / 0.45359237
        target_unit = "lb"
    else:
        print("Invalid input unit")
        return

    result = f"{value} {unit} = {converted_value:.2f} {target_unit}"
    print(result)

if __name__ == "__main__":
    input_str = input("Enter a distance or weight amount with units: ")
    convert_units(input_str)
