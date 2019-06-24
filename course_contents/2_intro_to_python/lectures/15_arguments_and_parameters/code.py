# Imagine you've got some code that calculates the fuel efficiency of a car:

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

mpg = car["mileage"] / car["fuel_consumed"]
name = f"{car['make']} {car['model']}"
print(f"{name} does {mpg} miles per gallon.")

# You could put this in a function:


def calculate_mpg():
    car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg()

# But this is not a very reusable function since it only calculates the mpg of a single car.
# What if we made it calculate the mpg of "any" arbitrary car?

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}


def calculate_mpg(car_to_calculate):  # This can be renamed to `car`
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg(car)

# This means that given a list of cars with the correct data format, we can run the function for all of them!

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    calculate_mpg(car)
