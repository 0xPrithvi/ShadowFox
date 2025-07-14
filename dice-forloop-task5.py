import random

rolls = 30  # You can change this to any number >= 20


count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0

previous_roll = None

print("Rolling the die:")
for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")

    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_two_6s_in_a_row += 1
    if roll == 1:
        count_1 += 1

    previous_roll = roll

print("\nStatistics:")
print(f"Number of times 6 was rolled: {count_6}")
print(f"Number of times 1 was rolled: {count_1}")
print(f"Number of times two 6s appeared in a row: {count_two_6s_in_a_row}")

