# Step 1: Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# Step 1: Count the number of members
print("Number of members:", len(justice_league))

# Step 2: Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)

# Step 3: Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to the beginning:", justice_league)

# Step 4: Separate Aquaman and Flash by adding Green Lantern between them
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

# Make sure Aquaman comes before Flash
if aquaman_index > flash_index:
    aquaman_index, flash_index = flash_index, aquaman_index

# Remove Green Lantern from current position
justice_league.remove("Green Lantern")

# Insert Green Lantern between Aquaman and Flash
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)

# Step 5: Replace entire list with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After replacing with new members:", justice_league)

# Step 6: Sort alphabetically
justice_league.sort()
print("After sorting alphabetically:", justice_league)

# BONUS: Predict new leader
print("New leader (0th index):", justice_league[0])
