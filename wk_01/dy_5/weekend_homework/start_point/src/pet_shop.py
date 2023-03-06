
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amt):
    pet_shop["admin"]["total_cash"] += amt
    return None

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num_sales):
    pet_shop["admin"]["pets_sold"] += num_sales
    return None

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, brd):
    return [x for x in pet_shop["pets"] if x["breed"] == brd]

""" def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    
    return found_pets
 """

def find_pet_by_name(pet_shop, nm):
    pets = pet_shop["pets"]
    named_pet = [x for x in pets if x["name"] == nm]
    if len(named_pet) == 0:
        return None
    return named_pet[0]

""" def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
 """ 

""" def find_pet_by_name(pet_shop, nm):
    found_pet = None
    for pet in pet_shop["pets"]:
        if pet["name"] == nm:
            found_pet = pet

    return found_pet
 """

def remove_pet_by_name(pet_shop, nm):
    pets = pet_shop["pets"]

    try: 
        pet_index = [x["name"] for x in pets].index(nm)
    except:
        return None
    
    pets.pop(pet_index)

    return None

# The following is the suggested solution (which is better)
# def remove_pet_by_name(pet_shop, name):
#     pet_to_delete(find_pet_by_name(pet_shop, name))
#     pet_shop["pets"].remove(pet_to_delete)

def add_pet_to_stock(pet_shop, nw_pt):
    pet_shop["pets"].append(nw_pt)
    return None

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amt):
    customer["cash"] -= amt
    return None

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
    return None

def customer_can_afford_pet(customer, pet):
    customer_cash = customer["cash"]
    pet_cost = pet["price"]
    return customer_cash >= pet_cost

def mug_customer(customer, mugger):
    customer_cash = customer["cash"]
    customer["cash"] = 0
    mugger["cash"] += customer_cash
    mugger["karma"] -= 1

def sell_pet_to_customer(pet_shop, pet, customer):
    # conditions to exit early:
    if pet is None:
        return None

    if customer_can_afford_pet(customer, pet) == False:
        return None

    # EACH OF THE FOLLOWING CAN BE REPLACED BY AN EXISTING FUNCTION! 
    # get the price 
    pet_price = pet["price"]
    # debit the customer 
    customer["cash"] -= pet_price
    # credit the pet shop
    pet_shop["admin"]["total_cash"] += pet_price
    # add pet to customer
    customer["pets"].append(pet)
    # add 1 to number of pets sold
    pet_shop["admin"]["pets_sold"] += 1 

    # n.b. this function doesn't actually remove 
    # pets from the inventory as it's not in the 
    # unit tests!

    # The following is not needed as None is returned 
    # if return keyword is not used
    return None