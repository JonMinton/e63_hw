def return_10():
    return 10

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def length_of_string(stng):
    return len(stng)

def join_string(str_1, str_2):
    return str_1 + str_2

def add_string_as_number(a, b):
    return int(a) + int(b)

def number_to_full_month_name(num):
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]
    return months[num - 1]

def number_to_short_month_name(num):
    months = [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun",
        "Jul", "Aug", "Sep",
        "Oct", "Nov", "Dec"
    ]
    return months[num - 1]


def calc_cube_volume(x):
    return pow(x, 3)

def reverse_string(string):
    return string[::-1]

def convert_f_to_c(temp_f):
    return (temp_f - 32 ) * 5 / 9