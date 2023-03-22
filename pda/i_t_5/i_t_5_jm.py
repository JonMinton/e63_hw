# # Introduction
# 
# **Jon Minton. E63**
# 
# This document addresses the task listed in I.T.5
# 
# The task is as described below:
# 
# ## Problem
# 
# Demonstrate the use of a list in a program. Include in your screenshot(s):
# 
# - A list in a program
# - A function (that you’ve created) that uses the list
# - The result of the function running
# 
#  
# 
# Submit a comment explaining your understanding of:
# 
# - The use of lists in programs
# - The code you’ve submitted
# 
#  
# 
# Remember:
# 
# - Show all relevant and referenced code in your screenshots
# - Use original work that is your own (i.e. no start/end code handed out as course materials (unless PDA specific), copied from the internet, or submitted by another student)
# - Reattach all files on any resubmission
# - Do NOT reuse examples from another submission
# 


# ## Solution
# 
# The following is python code which addresses the problem as described above:

# The line below this creates a list called 'my_list'. The elements of the list are not all of the same type, with the first being a string,
# the second an integer, the third and forth being Boolean values, and the last element being a float value. 
my_list = ["A", 52, True, False, 23.8]


# The contents of the list can be printed as follows:
print("Printing of a list object")

print(my_list)


# The code below creates a simple function, called get_length(). This function returns the length of the list.

def get_length(lst):
    return len(lst)

# The code below shows the result of applying the get_length() function to the my_list list object

print("The result of calling a function, get_length(), on the list created")
get_length(my_list)
print("n.b. the function alone will return nothing to the console, as it does not invoke print")

# The function returns the length of the list object passed to it. As the print function is not called, no output is 
# returned to the user. 
# Instead, the function's output can be saved to a new object, and that object can be printed. 


length_of_my_list = get_length(my_list)
print("Printing of an object which stores the result of the same function")
print(length_of_my_list)


# This confirms that the function has returned the value '5' which is the length of the list (i.e. the number of elements)
# it contains. 

# The type of the return value is not explicitly declared, but implicitly cast as of type integer. This can be confirmed as 
# follows:
print("Printing the result of calling the type function on the object created by the user-defined function get_length()")
print(type(length_of_my_list))


