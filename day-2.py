#Program to calculate how many days, weeks and months is left in your life

age = input("What is your current age?")

age = 90 - int(age)
days = age * 365
months = age * 12
weeks = age * 52

print(f"You have {days} days, {weeks} weeks and {months} months left")
