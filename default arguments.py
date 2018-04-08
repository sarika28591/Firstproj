def my_function(name , age):
    print("My name is " + name + " and my age is " + str(age))

my_function("nick" , 27)


def identity_function (name , age) :
    print ("My name is" , name , "and my age is" , age)

identity_function("mike" , 27)

def print_something(name = "something", age = "unknown"):
    print("My name is", name, "and my age is", age)

print_something("harry")


def identity_function (name , age) :
    print ("My name is" , name , "and my age is" , age)

identity_function("mike" , 24 + 1)


def identity_function (name , age) :
    print ("My name is" , name , "and my age is" , age)

identity_function("mike" , ["25" , "24"][0])


def identity_function (name , age) :
    print ("My name is" , name , "and my age is" , age)

identity_function("mike" , {"abc" :"xyz" , "def" :"asx"} ['abc'])