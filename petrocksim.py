Rock_Name = input(f"Welcome to Pet Rock Simulator, what would you like to name your new rock?")
age = 0
hunger = 5
happy = 5
print(f"Your new {Rock_Name} starts out with some stats, specifically, Age, Happiness and Hunger. Age starts at 1, but passively increases in vale each 'turn.' Hunger and Happiness each starts at 5/10. If hunger reaches 10, your rock will starve. If Happiness reaches 0, your Rock will run away.")
count = 0
while True:
    age += 1
    user_input = input(f"What would you like to do with your {Rock_Name} Today? (year {count}, your rock is {age}) 1. Play ({happy}/10) 2. Feed ({hunger}/10) 3. Nothing.")
    count += 1
    if age == 20:
        print(f"Your {Rock_Name} has died of old age and lived a very great life. Game Over")
        exit
    elif hunger == 10:
        print(f"{Rock_Name} has starved. How could you neglect them?")
        exit
    elif happy == 10:
        print(f"{Rock_Name} has become depressed and has run away to find a new life.")
        exit
    else:
        if user_input == "1":
            hunger += 1
            happy += 2
            print(f"You played with {Rock_Name}, +1 Hunger, +2 Happiness")
            continue
        elif user_input == "2":
            hunger -= 2
            happy -= 1
            print(f"You fed {Rock_Name}. -2 Hunger, -1 Happiness ")
            continue
        elif user_input == "3":
            hunger += 1
            happy -= 1
            print(f"you did nothing with {Rock_Name}. +1 Hunger, -1 Happiness")
            continue
        else:
            print(f"{Rock_Name} has no idea what you mean by this.")
            continue
    
