# AND: দুইটা condition ই True হলে result True হবে।
print(True and True)    # True
print(True and False)   # False
print(5 > 3 and 10 > 5) # True
print(5 > 3 and 2 > 8)  # False

#Rule:
#দুইটাই True → True
#একটা False হলেই → False


# OR: যেকোনো একটা True হলেই result True হবে।
print(True or False)    # True
print(False or False)   # False
print(5 > 10 or 8 > 3)  # True

#Rule:
#একটা True হলেই → True
#দুইটাই False → False


# NOT: True কে False করে, False কে True করে।
print(not True)         # False
print(not False)        # True
print(not 5 > 3)        # False
