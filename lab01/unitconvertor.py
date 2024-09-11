from random import choice


def metric_to_imperial(value, conversion_type):
    if conversion_type == "km to miles":
        return value * 0.621371
    elif conversion_type == "cm to inches":
        return value * 0.393701
    elif conversion_type == "meters to yards":
        return value * 1.09361
    elif conversion_type == "kg to pounds":
        return value * 2.20462
    elif conversion_type == "grams to oz":
        return value *0.035274

    else:
        return None

def imperial_to_metric(value, conversion_type):
    if conversion_type == "miles to km":
        return value / 0.621371
    elif conversion_type == "inches to cm":
        return value / 0.393701
    elif conversion_type == "yards to meters":
        return value / 1.09361
    elif conversion_type == "pounds to kg":
        return value / 2.20462
    elif conversion_type == "oz to grams":
        return value / 0.035274
    else:
        return None

def conversion_tool():
    print("Welcome to the Conversion Tool!")
    print("1. Metric to Imperial")
    print("2. Imperial to Metric")

    selection = input("Choose your conversion type (1 or 2): ")


    if selection == "1":
        print("Metric to Imperial Options:")
        print("a. Kilometers to Miles")
        print("b. Centimeters to inches")
        print("c. Meters to yards")
        print("d. Kilograms to Pounds")
        print("e. Grams to ounces")
        option = input("Choose conversion type (a,b,c,d, or e): ")

        if option == "a":
            value = float(input("Enter the value in kilometers: "))
            result = metric_to_imperial(value, "km to miles")
            print(f"{value} kilometers is equal to {result:.2f} miles.")

        elif option == "b":
            value = float(input("Enter the value in centimeters: "))
            result = metric_to_imperial(value, "cm to inches")
            print(f"{value} centimeters is equal to {result:.2f} inches.")

        elif option =="c":
            value = float(input("Enter the value in meters: "))
            result = metric_to_imperial(value, "meters to yards")
            print(f"{value} meters is equal to {result:.2f} yards.")

        elif option == "d":
            value = float(input("Enter the value in kilograms: "))
            result = metric_to_imperial(value, "kg to pounds")
            print(f"{value} kilograms is equal to {result:.2f} pounds.")

        elif option == "e":
            value = float(input("Enter the value in grams: "))
            result = metric_to_imperial(value, "grams to oz")
            print(f"{value} grams is equal to {result:.2f} ounces.")

    elif selection == "2":
        print("Imperial to Metric Options:")
        print("a. Miles to Kilometers")
        print("b. Inches to centimeters")
        print("c. Yards to meters")
        print("d. Pounds to kilograms")
        print("e. Ounces to grams")
        option = input("Choose conversion type (a,b,c,d, or e): ")

        if option == "a":
            value = float(input("Enter the value in miles: "))
            result = imperial_to_metric(value, "miles to km")
            print(f"{value} miles is equal to {result:.2f} kilometers.")

        elif option == "b":
            value = float(input("Enter the value in inches: "))
            result = imperial_to_metric(value, "inches to cm")
            print(f"{value} inches is equal to {result:.2f} cm.")

        elif option =="c":
            value = float(input("Enter the value in yards: "))
            result = imperial_to_metric(value, "yards to meters")
            print(f"{value} yards is equal to {result:.2f} meters.")

        elif option == "d":
            value = float(input("Enter the value in pounds: "))
            result = imperial_to_metric(value, "pounds to kg")
            print(f"{value} pounds is equal to {result:.2f} kilograms.")

        elif option == "e":
            value = float(input("Enter the value in ounces: "))
            result = imperial_to_metric(value, "oz to grams")
            print(f"{value} ounces is equal to {result:.2f} grams.")

    else:
        print("Invalid choice. Please try again.")

conversion_tool()
