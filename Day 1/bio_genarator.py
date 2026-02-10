# Build a simple Bio Genarator using user input and print().

name = input('What is your name? ')
age = input('How old are you? ')
city = input('Which city do you live in? ')
fact = input('Please share a fun fact about yourself!: ')

#print("\n--- Your Bio ---\n")
#print("Hi!, this is " +name+ "!")
#print("I am "+age+ "years old and I live in "+city+ ".")
#print("Fun fact about me: "+fact+".")

print("\n--- Your Bio ---\n")
print(f"Hi!, this is {name}!")
print(f"I am {age} years old and I live in {city}.")
print(f"Fun fact about me: {fact}.")