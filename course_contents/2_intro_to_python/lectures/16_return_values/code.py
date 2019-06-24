def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg  # Ends the function, gives back the value


def car_name(car):
    return f"{car['make']} {car['model']}"


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon.")
    # Returns None by default, as all functions do


cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    print_car_info(car)
    # try print(print_car_info(car)), you'll see None


# -- Multiple returns --


def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


print(divide(10, 2))  # 5
print(divide(6, 0))  # You tried to divide by zero!
