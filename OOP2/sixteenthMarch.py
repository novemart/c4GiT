def addition(a, b):
    print('Function called!')
    return a+b

a = 5
b = 3

result = addition(a, b)

if result > 10:
    print('Greater than 10', result)
elif result > 11:
    print('Greater than 11', result)
else:
    print('Smaller', result)
