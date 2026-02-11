#Python-এ indentation মানে হলো লাইন শুরুর আগে space দেওয়া।
#এটা শুধু সাজানোর জন্য না — এটা Python-এর syntax-এর অংশ।

#কেন Indentation দরকার?
#Python { } ব্যবহার করে না (C/Java এর মতো)। বরং indentation দিয়েই block বুঝে।

#Example
if 5 > 3:
    print("Correct")

#👉 Colon : এর পরে ৪টা space দেওয়া হয়েছে।

# Wrong Indentation
#if 5 > 3:
#print("Wrong")
#👉 এখানে indentation নেই → Error হবে (IndentationError)

#Same Block, Same Indentation
if 10 > 5:
    print("Line 1")
    print("Line 2")
    print("Line 3")

# Nested Indentation
age = 20

if age >= 18:
    print("Adult")
    
    if age < 30:
        print("Young Adult")
