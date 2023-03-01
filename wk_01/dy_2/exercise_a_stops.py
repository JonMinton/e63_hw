stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
print(stops)
#1. Add "Edinburgh Waverley" to the end of the list

print("Part 1: Add 'Edinburgh Waverley' to the end of the list")
stops.append("Edinburgh Waverley")
print(stops)

#2. Add "Glasgow Queen St" to the start of the list
print("Part 2: Add 'Glasgow Queen St' to the start of the list")
stops.insert(0, "Glasgow Queen St")
print(stops)

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
print("Part 3: Add 'Polmont' at the appropriate point (between 'Falkirk High' and 'Linlithgow')")
stops.insert(4, "Polmont")
print(stops)

#4. Print out the index position of "Linlithgow"
print("Part 4: Print out the index position of 'Linlithgow'")
print(stops.index("Linlithgow"))

#5. Remove "Livingston" from the list using its name
print("Part 5: Remove 'Livingston' from the list using its name")
stops.remove("Linlithgow")
print(stops)

#6. Delete "Cumbernauld" from the list by index
print("Part 6: Delete 'Cumbernauld' from the list by index")
del stops[stops.index("Cumbernauld")]
print(stops)

#7. Print the number of stops there are in the list
print("Part 7: Print the number of stops there are in the list")
print(len(stops))

#8. Sort the list alphabetically
print("Part 8: Sort the list alphabetically")
stops.sort()
print(stops)

#9. Reverse the positions of the stops in the list
print("Part 9: Reverse the positions of the stops in the list")
stops.reverse()
print(stops)

#10 Print out all the stops using a for loop

print("Part 10: Print ut all the stops using a for loop")
for stp in stops:
    print(stp)