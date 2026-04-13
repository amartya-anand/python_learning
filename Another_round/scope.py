# Global vs Local scope

def add_one(n):
    n = n + 1
    print(n)


n = 10  # n is a global variable

add_one(n)  # Output will be 11.

print(n)  # Output will be 10.

# Variables defined inside a function are local to that function.
# They cannot be accessed outside the function.

# Variables defined outside a function are global variables.
# They can be accessed inside the function.
