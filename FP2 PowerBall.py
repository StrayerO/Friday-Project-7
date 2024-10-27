import random
import time

# Display welcome message
print("Welcome to the PowerBall number generator.")

# Print two empty lines
print("\n")

# Display the starting message without newline
print("Your PowerBall numbers are: ", end="", flush=True)

# Generate and display first 5 numbers
for i in range(5):
    number = random.randint(1, 69)
    print(f"{number}", end=" ", flush=True)
    time.sleep(0.5)

# Add extra spaces before PowerBall number
print("  ", end="", flush=True)

# Wait 3 seconds
time.sleep(1)

# Generate and display PowerBall number in red using ANSI escape codes
powerball = random.randint(1, 26)
print(f"\033[91m{powerball}\033[0m")

# Display ending message
print("\nThank you for stopping by.")