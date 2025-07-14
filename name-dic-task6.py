
friends = ["Mahesh", "Prithvi", "Sujay", "Darshan", "Jovin"]

name_length_tuples = [(name, len(name)) for name in friends]

print("List of (Name, Length) tuples:")
for item in name_length_tuples:
    print(item)
