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


def all_favourite_foods(ppl):
    all_foods = []

    for person in ppl: 
        all_this_persons_foods = person["favourites"]["snacks"]
        all_foods += all_this_persons_foods

    return all_foods

def find_no_friends(ppl):
    persons_with_no_friends = []

    for person in ppl:
        print(persons_with_no_friends)
        persons_friends = person["friends"]
        if len(persons_friends) == 0:
            persons_with_no_friends.append(person)

    return persons_with_no_friends

def unique_favourite_tv_shows(ppl):
    all_tv_shows = [] 

    for person in ppl:
        all_tv_shows.append(person["favourites"]["tv_show"])

    all_tv_shows = list(set(all_tv_shows))
    all_tv_shows.sort()
    return all_tv_shows    