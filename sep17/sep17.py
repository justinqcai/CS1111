# my_variable_name = "justin" #ok
# myVariableName = "justin" #not good practice
#
# print(int(1.3))
# print(int(float('1.3')))
#
# print(bool(1.3))
# print(bool('upsorn'))
#
# print(420000)
# print(42,"000")
# print("42" + "," + "000")
#
# print(10.0/4)
# print(10.0//4)
# print(10//4)
#
# print(format(1234.5678, ".2f"))
# print(format(1234.5678, ".9f"))
# print(format(1234.5678, ".2%"))
# print("{:.3f}".format(123456789))
# print("{:10d}".format(123456789))
#
# print("number1 = %5d, number2 = %4.2f" % (123, 98765.4321))
# print("number1 = %5d, number2 = %8.2f" % (123, 98765.4321))
# print("number1 = %5d, number2 = %9.2f" % (123, 98765.4321))
#
# your_name = input("What is your name? ")
# print("Hello, " + your_name)
#
# num1 = int(input('Enter the first number : '))
# num2 = int(input('Enter the second number : '))
# print(num1+num2)

#
# def add(num1, num2):
#     print("I am adding " + str(num1) + " and " + str(num2))
#     return num1 + num2
#
# x = add(2,3)
# print(x)


def getBigger(num1, num2):
    result = ""
    if num1 > num2:
        print(num1)
        result = num1
    else:
        print(num2)
        result = num2
    return result


getBigger(31, 26)