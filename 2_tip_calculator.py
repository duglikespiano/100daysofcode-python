print("Welcome to the tip calculator.")

bill_cost = round(float(input("What was the total bill? $ ")), 2)
tip_percentage = round(
    float(input("What percentage tip would you like to give? ")), 2)/100
how_many_people = round(float(input('How many people to split the bill? ')), 0)

cost_with_tip = round(bill_cost/how_many_people*(1+tip_percentage), 2)

print(f"Each person should pay : ${cost_with_tip}\n")
