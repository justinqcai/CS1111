#print("hello", "world")

#print("hello" * 3)  #string * int will print the str however many times the int is

# print("hello" *3.4)

#print(type("hello")) # type tells you what type the variable is
#print(type("3"))

#print(type(int(("3"))))

# Exercise: data type
# # Date: Sep 7, 2016

# 1. Consider the following statements. What are data types?
hungry = True                   # a. boolean
sleepy = True                   # b. boolean
have_another_class = False      # c. bool



print("<-- question 2 -->")
# 2. What do we get from the following statement? What data type?
# Note: You are expected to know a simple truth table (and, or, not)
print(hungry == sleepy)         # a. true, bool
print(hungry and sleepy)        # b. true, bool
print(hungry and sleepy and have_another_class)   # c. false, bool
print(hungry != sleepy and have_another_class)    # d. false, bool
#print(hungry == True and == sleepy)                # e.




print("<-- question 3 -->")
# 3. Write a statement that displays a string "hungry" 4 times using an * operator

print("hungry" * 4)



print("<-- question 4 -->")
# 4. Consider the following statements. What do we get?
string = "This is my name!"
number = 3

# What are data types?
print(type(number))              # a.
print(type(str(number)))         # b.
# Notice how the type was changed

floater = number + 4.34

# What type do we get when adding a float and an integer?
print(type(floater))             # c.

print(type(int(floater)))        # d.
print(type(number + 3))          # e.

print(type(number == 4))         # f.
print(number == 4)               # g.
print((number == 4) == False)    # h.
print(type((number == 4) == False))   # i.

print(number < 4)                     # j.

print(number < 4 and type(number) == type(3))   # k.

print(number > 5 or type(number) == type(3))    # l.

print(type(type(number == 4)))                  # m.

print(type(number) is int)                      # n.



print("<-- question 5 -->")
# 5. Consdier the following statements
a = 'python'
b = "".join(['py', 'thon'])
print(a)                    # a.
print(b)                    # b.

print(a == b)               # c.
print(a is b)               # d.

# now, let's reassign
a = b
print(a == b)               # e.
print(a is b)               # f.
# Why are #d and #f different?
