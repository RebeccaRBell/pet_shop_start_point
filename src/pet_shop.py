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
    for pets in shop["pets"]:
        if pets["name"] == name:
            shop["pets"].append(pets)


def add_pet_to_stock(shop, pet):
    shop["pets"].insert(pet)
