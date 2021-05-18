# Program to enrypt and decrypt in ceasar cipher

user_input = input("Type 1 for encrypt and 2 for decrypt: ")
if user_input not in ["1", "2"]:
    print("Invalid input.")
    exit()

message = input("Type your message: ")

shift = input("Type the shift number: ")
if not shift.isdigit():
    print("Invalid shift number.")
    exit()

if user_input == "1":
    print("Encoded result: " + "".join([chr(ord(i) + int(shift)) for i in message]))

elif user_input == "2":
    print("Decoded result: " + "".join([chr(ord(i) - int(shift)) for i in message]))
