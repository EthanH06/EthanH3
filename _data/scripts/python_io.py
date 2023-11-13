# Python I/O Part
echo -e "\nPython I/O Example:"
python3 - <<EOF
# Python code for user input and game logic
guess = int(input("Enter your guess (1-100): "))
if guess == $random_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number was {random_number}. Try again.")
EOF
