your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your total expenses: ₹{your_total}")
print(f"Partner's total expenses: ₹{partner_total}")

if your_total > partner_total:
    print("You spent more than your partner.")
elif your_total < partner_total:
    print("Your partner spent more than you.")
else:
    print("Both of you spent the same amount.")

max_diff = 0
significant_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_diff:
        max_diff = difference
        significant_category = category

print(f"Biggest spending difference is in '{significant_category}' with a difference of ₹{max_diff}.")
