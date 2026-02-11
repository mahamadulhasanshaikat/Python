# Logical conditionals মানে হলো — একাধিক condition একসাথে ব্যবহার করা। (and,or,not)

#Real Example
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

#Multiple Logical Condition
age = 22
student = True

if age > 18 and student == True:
    print("Eligible for Student Offer")
