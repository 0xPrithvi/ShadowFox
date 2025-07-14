total_jumping_jacks = 100
done_jumping_jacks = 0
set_size = 10

while done_jumping_jacks < total_jumping_jacks:
    # Perform 10 jumping jacks
    done_jumping_jacks += set_size
    print(f"\nYou completed {done_jumping_jacks} jumping jacks.")
    
    # Check if goal is already reached
    if done_jumping_jacks >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    # Ask if user is tired
    tired = input("Are you tired? (yes/no): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"\nYou completed a total of {done_jumping_jacks} jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - done_jumping_jacks
            print(f"{remaining} jumping jacks remaining. Keep going!")
    elif tired in ["no", "n"]:
        remaining = total_jumping_jacks - done_jumping_jacks
        print(f"{remaining} jumping jacks remaining. Let's continue!")
    else:
        print("Invalid input, assuming you're ready to continue!")
