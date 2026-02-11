#multiplication table generator

num = int(input("Enter a number to print its multiplication table: "))
print(f"\nMultiplication table of {num}:\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
