# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_nos = [num for num in numbers if num % 2 == 0]
print(even_nos)

# 2. Print the difference between the largest and smallest value:

print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

N = len(numbers) - 1
i = 0

while i < N:
    if (numbers[i] == 2) and (numbers[i+1] == 2):
        print(True)
    i += 1

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

cond_sum_numbers = 0 
add_these_numbers = True

for i in range(len(numbers)): 
    this_num = numbers[i]

    if this_num == 6:
        add_these_numbers = False

    if add_these_numbers == False: 
        if i > 0:
            last_num = numbers[i-1]
            if last_num == 7:
                add_these_numbers = True

    if add_these_numbers:
        cond_sum_numbers += this_num

        
print(cond_sum_numbers)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

cond_sum_numbers = 0
add_these_numbers = True

for i in range(len(numbers)):
    this_num = numbers[i]

    if this_num == 13:
        add_these_numbers = False
    
    if i > 0 and this_num != 13:
        last_num = numbers[i-1]
        if last_num == 13:
            add_these_numbers = False
        else:
            add_these_numbers = True

    if add_these_numbers:
        cond_sum_numbers += this_num
    
    print(f"i is {i} and this_num is {this_num}, and sum so far is {cond_sum_numbers} and flag is {add_these_numbers}")




print(cond_sum_numbers)