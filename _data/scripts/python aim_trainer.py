import random

def main():
    print("Welcome to the Personal Aim Trainer!")
    total_shots = 0
    successful_shots = 0

    while True:
        input("Press Enter to shoot...")
        
        # Generate a random target (a number between 1 and 100)
        target = random.randint(1, 100)
        total_shots += 1

        print("Target:")
        print(" " * (target - 1) + "*")  # Display the target as an asterisk with spacing
        guess = int(input("Enter your guess (1-100): "))

        if guess == target:
            print("Congratulations! You hit the target.")
            successful_shots += 1
        else:
            print(f"Missed. The target was at {target}.")

        accuracy = (successful_shots / total_shots) * 100
        print(f"Accuracy: {accuracy:.2f}%")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for using the Personal Aim Trainer!")

if __name__ == "__main__":
    main()
