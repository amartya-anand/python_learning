def display_days():

    days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    for day in days_list:

        print(day)


# function call

display_days()


def greet():

    print(f"Good Morning, {username} !")


# get username from user

username = input("Enter User Name:")

# function call

greet()

# Factorial


def facto(x):

    if x == 0:

        return 1

    else:

        return (x*facto(x-1))

# lets calculate factorial of 4


four_fact = facto(4)

print(four_fact)

# lets calculate factorial of 3

three_fact = facto(3)

print(three_fact)

num = int(input("Enter a number: "))

factorial = 1

if num < 0:

    print(" Factorial does not exist for negative numbers")

elif num == 0:

    print("The factorial of 0 is 1")

else:

    for i in range(1, num + 1):

        factorial = factorial*i

    print("The factorial of", num, "is", factorial)


def two_nums_add():

    # calculate addition

    addition = num1+num2

    # return the addition

    return (addition)

# lets define two variables


num1 = 10

num2 = 20

# function call and store the sum in result variable

result = two_nums_add()

print(f"Their addition(num1+num2): {result}")


def calculate():

    # calculate sum

    addition = num1+num2

    # calculate product

    product = num1*num2

    # return sum and product

    return (addition, product)

# lets define two variables


num1 = 10

num2 = 20


# Lets store sum inside num_add variable

# and product inside num_prod

num_add, num_prod = calculate()

print(f'Their addition(num1+num2): {num_add}')

print(f'Their product(num1*num2): {num_prod}')


def add_numbers(num1, num2):

    print(f'first number:{num1}')

    print(f'second number:{num2}')

    result = num1+num2

    print(f'their addition:{result}')


a = 10

b = 40

add_numbers(a, b)


def attendance(name1, name2, name3):

    print(f'Roll number one:{name1}')

    print(f'Roll number two:{name2}')

    print(f'Roll number three:{name3}')

    print(f'Attendance completed ...\n')


a = 'Raj'

b = 'Pooja'

c = 'Kamal'

attendance(a, b, c)

attendance(c, b, a)

attendance(b, a, c)

# Global variables

my_num = int(input("please enter number:"))


def make_twice():

    print('lets make it twice:')
    print(my_num*2)


print(f"Your number is:{my_num}")

make_twice()

# Local variables

my_num = int(input("please enter number:"))


def multiply():

    loc_num = 100

    print('lets multiply with local variable:')

    print(my_num*loc_num)


multiply()

print(f"global variable is:{my_num}")

# print(f"local variable is:{loc_num}") # Local variable is not available

# *args


def add_nums(*args):

    print('Positional arguments passed to the function are:')
    print(args)

    result = sum(args)

    return result


result = add_nums(10, 20, 30, 40)

print(f'The numbers addition: {result}')

# **kwargs


def add_nums(**kwargs):

    print('Keyword arguments passed to the function are:')

    print(kwargs)

    result = sum(kwargs.values())

    return result


result = add_nums(num1=10, num2=20, num3=30, num4=40)

print(f'The numbers addition: {result}')

# Both arbitrary arguments


def add_nums(*args, **kwargs):

    print('Positional arguments passed to the function are:')

    print(args)

    print('Keyword arguments passed to the function are:')

    print(kwargs)

    result1 = sum(args)

    result2 = sum(kwargs.values())

    return result1, result2


pos1 = 1

pos2 = 2

pos3 = 3

pos4 = 4

result1, result2 = add_nums(pos1, pos2, pos3, pos4,
                            num1=10, num2=20, num3=30, num4=40)

print(f'The positional argument numbers addition: {result1}')

print(f'The keyword argument numbers addition: {result2}')

# Global vs Local

my_num = int(input("please enter number:"))


def twice():

    print(' --- local scope ---')

    global my_num

    my_num = 150

    print(f"global variable in local scope:{my_num}")

    print(f'lets make it twice:{my_num*2}')


twice()

print(' --- global scope ---')

print(f"global variable in global scope:{my_num}")
