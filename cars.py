# Create a dictionary of available cars and their sales prices
available_cars = {
    "benz": 70000,
    "hellcat": 85000,
    "ford": 90000,
    "chevrolet": 60000,
    "trackhawk": 150000
}

# Prompt the user to enter their car brand
car_brand = input("Enter your car brand: ")

# Check if the car brand is in the dictionary of available cars
if car_brand in available_cars:
    print(f"{car_brand} is available for sale!")
    print(f"The sales price of {car_brand} is ${available_cars[car_brand]}")
else:
    print(f"Sorry, {car_brand} is not available for sale.")