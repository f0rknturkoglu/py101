# LAMBDA FUNCTIONS

def x(a): return a + 10


print(x(5))


def x(a, b): return a*b


print(x(5, 6))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))


# lambda with build in functions


numbers = [2, 3, 4, 5, 1, 2]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

# using lambda with filter()

students = [('John', 88), ('Emma', 92), ('Sam', 75), ('Olivia', 95)]
passed_students = list(filter(lambda student: student[1] >= 80, students))
print(passed_students)


words = ["apple", "pie", "banaaaaaaaaaana", "cheeerry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# Python recursion

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)


countdown(5)


def factorial(n):
    # BASE CASE
    if n == 1 or n == 0:
        return 1
    else:
        # RECURSIVE CASE
        return n * factorial(n-1)


print(factorial(5))


# FIBONACCI SERIES

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


# recursion with list

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])


my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
# OUTPUT: 15
