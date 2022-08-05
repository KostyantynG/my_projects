calculation_to_units = 24 * 60
name_of_unit = "minutes"


def days_to_units(num_of_days):
        return f"{num_of_days} days is {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)

        # we want to make conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered zero, no conversion for you!")
        else:
            print("You entered a negative number. No conversion for you!")

    except ValueError:
        print("Your input is not valid a number, don't ruin my program")


user_input = ""
while user_input != "stop":
    user_input = input("Enter number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)


