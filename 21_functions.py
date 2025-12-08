def my_function():
    print("This is my function.")

    pass

my_function()
my_function()
my_function()

def get_greeting():
    return "Hello, World!"

greeting = get_greeting()
print(greeting)
print(get_greeting())

#bir fonksiyon return statementne sahip değilse, None döner
def my_other_function():
    pass

result = my_other_function()
print(result)  # None yazdırır


##arguments##

def myfunc_with_arguments(fname):
    print(fname+'turkoglu')

myfunc_with_arguments("furkan ")

# -parameters vs arguments 
# parameters: fonksiyon tanımlanırken kullanılan değişken isimleridir.
# arguments: fonksiyon çağrılırken verilen gerçek değerlerdir.

def myfunc_with_multiple_arguments(fname, lname): #fname lname is a parameter
    print(fname + ' ' + lname)


myfunc_with_multiple_arguments("furkan", "turkoglu")
myfunc_with_multiple_arguments("ali", "veli") #ali veli argument'tir.


##Default parameter values##

def myfunc_with_default_parameter(country = "Norway"):
    print("I am from " + country)


myfunc_with_default_parameter("Sweden")
myfunc_with_default_parameter("India")
myfunc_with_default_parameter() #burda norway default olarak gelir


##keyword arguments

def myfunc_with_keyword_arguments(child3, child2, child1):
    print("The youngest child is " + child3)

myfunc_with_keyword_arguments(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
myfunc_with_keyword_arguments(child2 = "Tobias", child1 = "Emil", child3 = "Linus")


##positional arguments##

def my_function2(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function2(animal = "dog", name = "Buddy")


##mixing positional and keyword arguments##

def my_function3(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function3("dog", name = "Buddy", age = 5)

