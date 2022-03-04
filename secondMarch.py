import random
# #{} will create a dictionary
# set_numbers = set()
# for i in range(6)
# while len(set_numbers) <6:
#     numb = random.randint(1, 51)
#     set_numbers.add(numb)
# print(set_numbers)
#
# #list comprehension
# my_list = [i*4 for i in range(6)]
# print(my_list)
#
# random.sample(range(0, 50), 6)
# my_list = list(range(1,51))
# print(my_list)
# random.shuffle(my_list)
# print(my_list)
# print(my_list[0:6])
#
# fileObj = open('martina.txt','a')
#
# #print(fileObj.read())
# #my_file_list = fileObj.readlines()
# #print(my_file_list[2])
# fileObj.write("Hello from the code!")
# fileObj.close()


#function declaration
# def my_function():
#     print('hello')
#     print('you\'re in the function')
#
#
# for i in range(5):
#     #calling the function with this name
#     my_function()


# def addition(num1, num2):
#     solution = num1+num2
#     #return num1+ num2
#     return solution
#
# #to capture the returned value
# res = addition(6, 9)
# print(res)
#
# a = 15
# b = 89
# res = addition(a, b-3)
# print(res)
#
# def multiplyString(str):
#     #local scope
#     times = int(input("How many times? "))
#     #print(str*times)
#     return str*times
#
#
# res = multiplyString("hello")
# print(res)
# don't have access to times
#print(times)


# def modifyList(param_list):
#     param_list += ['bananas']
#
#
# my_list = ['apples', 'oranges']
# modifyList(my_list)
# print(my_list)

# def calculate_vat(price, tax=0.2, postage=2.0):
#     price2 = price + postage
#     return price2*tax
#
#
# print(calculate_vat(10))
# print(calculate_vat(13, 0.15))
# print(calculate_vat(postage=3, price=10, tax=0.1))

# def create_name(*, firstName, lastName):
#     return firstName + " " + lastName
#
#
# myName = create_name(firstName='Martina', lastName='Yusuf')
# #will throw an error
# #myName = create_name('Jane','Doe')
# print(myName)

#unpacking tuple
# a, b, c = (3, 6, 8)
# a, *b = (3, 6, 8)
# print(a)
# print(b)

# def create_name(firstName, lastName):
#     return firstName, 'Anne', lastName, len(firstName), len(lastName)
#
# res = create_name('Martina','Yusuf')
# print(res)

my_global_var = 7


def multiplyString(str):
    #local scope
    #times = int(input("How many times? "))
    global my_global_var
    my_global_var = 8
    #print(str*times)
    return str*my_global_var


my_global_var = 3
print(my_global_var)
res = multiplyString("hello")
print(my_global_var)
print(res)
#don't have access to times
# print(times)

