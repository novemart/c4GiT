
# if b != 0:
#     print(a/b)
# else:
#     print('you cant devide by zero silly!')

a = 4
b = 0

try:
    print(a/b)
except ZeroDivisionError as err:
    #handle the exception
    print("Something went wrong")
except FileNotFoundError as fnf:
    print('File not found')
except Exception:
    print("Other errors happened.")
# these two parts are optional
else:
    print("No exception happened!")
finally:
    print("This is printed all the time.")