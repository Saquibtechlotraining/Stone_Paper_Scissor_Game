while True:
    import random
    option_list = ["stone", "paper", "scissor"]
    for option in option_list:
        random.shuffle(option_list)   # Shuffle the list, so a computer choice any random word from a given list
    comp_choice = option

    print(".......(stone, paper, scissor) Game Begins.......")
    x = """    1. Do you want to play again
    2. Do you want to Exit the Game
    """
    print(x)
    ch = int(input("Enter Your Choice:"))
    print("Choose any Option")

    if ch == 1:
        print("Lets Play Again")

        print("Choose Your Game Level")
        y = """        1. Easy 
        2. Medium
        3. Hard"""
        print(y)

        select = int(input("Enter the Level:"))
        print("Select any 1 choice:", option_list)

        if select == 1:
            print("You Choose Easy Level")
            end = 15
            total_score = 150

        elif select == 2:
            print("You Choose Medium Level")
            end = 10
            total_score = 100

        elif select == 3:
            print("You Choose Hard Level")
            end = 5
            total_score = 50

        else:
            pass

        user_score = 0
        comp_score = 0

        print(f"Total Chances you got: {end}")    # Total Chances you got
        print(f"Total Score of this level: {total_score}")

        start = 1
        while (start <= end):
            user_choice = input("Enter the user choice:").lower()
            print(f"Chances left: {end - start}")    # Chances Left

            if user_choice == "paper"  and comp_choice == "stone":
                comp_choice = option
                print("Computer Choice:", comp_choice)
                print("You Won")
                user_score = user_score + 10
                print(f"Your Score:{user_score}")


            elif user_choice == "stone" and comp_choice == "scissor":
                comp_choice = option
                print("Computer Choice:", comp_choice)
                print("You Won")
                user_score = user_score + 10
                print(f"Your Score:{user_score}")


            elif user_choice == "scissor" and comp_choice == "paper":
                comp_choice = option
                print("Computer Choice:", comp_choice)
                print("You Won")
                user_score = user_score + 10
                print(f"Your Score:{user_score}")


            elif user_choice == comp_choice:
                comp_choice = option
                print("Computer Choice:", comp_choice)
                print("Game is Tie")
                print("Tie No Score for both You and computer")

            else:
                comp_choice = option
                print(f"Computer Choice: {comp_choice}")
                print("Computer Won")
                comp_score = comp_score + 10
                print(f"Computer Score: {comp_score}")
            start = start + 1
        if comp_score < user_score:
            print("You Won Final Match")

        elif comp_score > user_score:
            print("Computer Won Final Match")

        else:
            print("Match Tie")

    else:
        print("Thank You for play the Game")
        break

