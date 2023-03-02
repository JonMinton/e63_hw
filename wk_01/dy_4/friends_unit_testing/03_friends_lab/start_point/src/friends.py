def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, proposed_food):
    snacks = person["favourites"]["snacks"]

    for snack in snacks:
        if snack == proposed_food:
            return True

    return False

def add_friend(person, new_friend):
    person["friends"].append(new_friend)
    return None

def remove_friend(person, new_unfriend):
    friends = person["friends"]
    del friends[friends.index(new_unfriend)]
    return None

def total_money(people):
    total_money = 0

    for person in people:
        this_persons_money = person["monies"]
        total_money += this_persons_money

    return total_money


def lend_money(p1, p2, amt):
    p1["monies"] = p1["monies"] - amt
    p2["monies"] = p2["monies"] + amt
    return None


