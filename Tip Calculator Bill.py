print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
calc = tip / 100
abc = (bill * calc)
cal = (bill + abc)
total = cal / people
print(f"Each person should pay: ${total}")