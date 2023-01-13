# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]


def get_total_cash(shop):
    return shop["admin"]["total_cash"]


def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, number_sold):
    shop["admin"]["pets_sold"] += number_sold


def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed):
    number_of_breed = []
    for pets in shop["pets"]:
        if pets["breed"] == breed:
            number_of_breed.append(pets)
    return number_of_breed


def find_pet_by_name(shop, name):
    for pets in shop["pets"]:
        if pets["name"] == name:
            return pets


def remove_pet_by_name(shop, name):
    pet_to_delete = find_pet_by_name(shop, name)
    shop["pets"].remove(pet_to_delete)


def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, money):
    customer["cash"] -= money


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)


def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]


def sell_pet_to_customer(shop, pet, customer):
    if pet in shop["pets"]:
        if customer_can_afford_pet(customer, pet) == True:
            add_pet_to_customer(customer, pet)
            remove_customer_cash(customer, pet["price"])
            add_or_remove_cash(shop, pet["price"])
            increase_pets_sold(shop, 1)
            remove_pet_by_name(shop, pet["name"])
