import random

def get_user_numbers():
    print("Enter your 10 unique numbers (between 1 and 50):")
    user_numbers = set()

    while len(user_numbers) < 10:
        try:
            num = int(input(f"Enter number {len(user_numbers) + 1}: "))
            if 1 <= num <= 50:
                if num not in user_numbers:
                    user_numbers.add(num)
                else:
                    print("Number already entered. Choose a different number.")
            else:
                print("Number must be between 1 and 50.")
        except ValueError:
            print("Please enter a valid number.")

    return user_numbers


def play_game():
    # Generate game numbers
    game_numbers = random.sample(range(1, 51), 10)

    # Get user numbers
    user_numbers = get_user_numbers()
    user_marked = set()

    # Computer numbers
    computer_numbers = set(random.sample(range(1, 51), 10))
    computer_marked = set()

    print("\n Game Numbers Generated (Hidden, will be called one by one)")
    print("\nYour Numbers:", sorted(user_numbers))
    print("Computer Numbers:", sorted(computer_numbers))

    print("\n Number Calling Starts...\n")

    user_winner = False
    computer_winner = False

    for number in game_numbers:
        input("Press Enter to call next number...")
        print(f"Number Called: {number}")

        # Check User
        if number in user_numbers:
            user_marked.add(number)
            print("You marked", number)

        # Check Computer
        if number in computer_numbers:
            computer_marked.add(number)
            print("Computer marked", number)

        print(f"Your matched count: {len(user_marked)}/10")
        print(f"Computer matched count: {len(computer_marked)}/10")
        print("-" * 40)

    # Final Result
    if user_marked == user_numbers:
        user_winner = True
    if computer_marked == computer_numbers:
        computer_winner = True

    print("\n Game Over!\n")

    if user_winner and computer_winner:
        print(" It's a DRAW!")
    elif user_winner:
        print(" Congratulations! You WIN!")
    elif computer_winner:
        print(" Computer Wins!")
    else:
        print("No one matched all 10 numbers.")


if __name__ == "__main__":
    play_game()
