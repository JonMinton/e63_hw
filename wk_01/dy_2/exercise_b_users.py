users = {
    "Jonathan": {
        "twitter": "jonnyt",
        "lottery_numbers": [6, 12, 49, 33, 45, 20],
        "home_town": "Stirling",
        "pets": [
            {
              "name": "fluffy",
              "species": "cat"
            },
            {
              "name": "fido",
              "species": "dog"
            },
            {
              "name": "spike",
              "species": "dog"
            }
        ]
    },
    "Erik": {
        "twitter": "eriksf",
        "lottery_numbers": [18, 34, 8, 11, 24],
        "home_town": "Linlithgow",
        "pets": [
            {
              "name": "nemo",
              "species": "fish"
            },
            {
              "name": "kevin",
              "species": "fish"
            },
            {
              "name": "spike",
              "species": "dog"
            },
            {
              "name": "rupert",
              "species": "parrot"
            }
        ]
    },
    "Avril": {
        "twitter": "bridgpally",
        "lottery_numbers": [12, 14, 33, 38, 9, 25],
        "home_town": "Dunbar",
        "pets": [
            {
              "name": "monty",
              "species": "snake"
            }
        ]
    }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])
# 2. Get Erik's hometown
print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])

# # 5. Get the smallest of Erik's lottery numbers
print(min(users["Erik"]["lottery_numbers"]))

# # 6. Return an list of Avril's lottery numbers that are even

# # source: https://www.geeksforgeeks.org/python-program-to-print-even-numbers-in-a-list/
lst = users["Avril"]["lottery_numbers"]
even_nos = [num for num in lst if num % 2 == 0]
print(even_nos)

# # 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# # 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"])

# # 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({'name':'fluffy', 'species':'dog'})
print(users["Erik"]["pets"])

# # 10. Add another person to the users dictionary
users["Jane"] =  {
        "twitter": "janey",
        "lottery_numbers": [1, 2, 3, 4, 5, 6],
        "home_town": "Moonville",
        "pets": [
            {
              "name": "muffin",
              "species": "puffin"
            }
        ]
    }

print(users)