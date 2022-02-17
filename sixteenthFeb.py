# number = 0
# while number != 5:
#     number = int(input("give me a number: "))
#
# operator = input("give me an operator: ")
#
# if (operator == '+') or (operator == '-') or (operator == '/'):
#     print("good operator")
# else:
#     print("bad operator")

# lights = 'green'
# if lights == 'red':
#     pass
# else:
#     print("go")
#
# while lights == 'green':
#     pass


# my_list = [1,2,3,4,5,6]
# new_list = []
#
# for num in my_list:
#     num = num-1
#     print(num)
#
# print(my_list)
#
# for num in my_list:
#     new_list.append(num-1)
#
# print(new_list)
#
# for i, num in enumerate(my_list):
#     my_list[i] = my_list[i]-1
#
# print(my_list)

# counter = 0
# while counter<5:
#     print("Hello")
#     counter += 1
#     #counter = counter +1
#
# my_list = [0, 1, 2, 3, 4]
# for elem in my_list:
#     print("Hello from list")
#
# for i in range(0, 15, 3):
#     print(i, "hello from range")

# val1 = 8
# val2 = 5
# if a > b:
#     c = a
# else:
#     c = b
# conditional expression
# c = val1 if val1>val2 else val2
#
# result = 'same' if val1 == val2 else 'not the same'
# print(c)
# print(result)

# while True:
#     print("hello")


# print("\U0001F600")
# print("\N{winking face}")
#
# name = 'Martina'
# surname = "O'Donnel"
# surname2 = 'O\'Donnel'
# raw_white_space = r'\n'
# print(raw_white_space)
# num = 5
# print(name + " " + surname, end="; ")
# print(name, surname, num, sep="\U0001F600")
#
# text = "this is \t tab"
# print(text)
#
# quote = r'\''
# print(quote)

#string are immutable
# str = "Martina"
# str = str + "\U0001F600"
# print(str)
#
# name = "Martina"
#
# for ch in name:
#     print(ch)
#
# print(name[4])
# #name[4] = 'y'
#
#
# superLongText = """ this is super
# long
# string
# """
# print(superLongText)

str = "Hello World!"
# print(len(str))
#
# print(str.lower())
#
# print(str.rstrip())

# print(4*5)
#
# print("hello"*5)
#
# if "ello" in str:
#     print("its in there")

# print(str[3:9])
# print(str[-1])
# print(str[-5:-1])
#
# print(str[:10])
# print(str[3:])
#
# print(str[:])

split_str = "oranges,apples,bananas,milk"
print(split_str[8:14])

list_str = split_str.split(',')
print(list_str[1])

new_str = ":".join(list_str)
print(new_str)