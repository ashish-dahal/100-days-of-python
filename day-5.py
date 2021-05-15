# Fizz Buzz program
output = ""
for item in range(1, 101):
    output = item
    if item % 3 == 0:
        output = "Fizz"
    if item % 5 == 0:
        try:
            output += " Buzz"
        except:
            output = "Buzz"
    print(output)
