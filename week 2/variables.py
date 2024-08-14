# Variables
print("===== Variables =====")
a = 33
a = "test" # Redeclaring a variable with a different type.
# Invalid variable names
# $a = 33
# 2a = 33
print(a)

HELLO_WORLD = "Hello World"
print(HELLO_WORLD)

# Duck Typing
# If some method/property exists, then it doesn't matter what the type is.
# It can still be used.
print("===== Duck Typing =====")
some_dict_1 = {
    "name": "hello 1",
}

some_dict_2 = {
    "name": "hello 2",
    "age": 33,
}

def print_name(some_dict):
    print(some_dict["name"]) # This will work for both dicts since they have a "name" key.
    
print_name(some_dict_1)
print_name(some_dict_2)
