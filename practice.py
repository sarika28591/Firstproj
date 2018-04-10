def first_function():
    print("one")

first_function()



def first_function(str1 , str2):
    print(str1)
    print(str2)

first_function("ssvvs" , "asdsadsad")


def first_function(name , age):
    print("my name is " + name + " my age is " + str(age))

first_function("ssvvs" , 52)


string = 'rac'
print(string)
string_reversed = string[-1::-1]
print(string_reversed)

string = 'madam'
print(string)
string_reversed = string[-1::-1]
print(string_reversed)


string = 'madam ma I'
print(string)
string_reversed = string[-1::-1]
print(string_reversed)

string = 'Was It A Rat I Saw?'
print(string)
string_reversed = string[-1::-1]
print(string_reversed)


#calci

import re

print("Magical calculator")
print("Enter 'quit' to exit")

previous = 0
run = True

def my_function():
    global run
    global previous
    equation = ""
    if previous == 0:
       equation = input("enter equation :")
    else:
       equation = input(str(previous))

    if equation == 'quit':
        print("goodbye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.\()" "]', '', equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)


while run:
     my_function()
