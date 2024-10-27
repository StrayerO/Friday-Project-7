# Define color functions using ANSI escape codes
def blue_text(text):
    return f"\033[94m{text}\033[0m"

def red_text(text):
    return f"\033[91m{text}\033[0m"

def green_text(text):
    return f"\033[92m{text}\033[0m"

def yellow_text(text):
    return f"\033[93m{text}\033[0m"

def purple_text(text):
    return f"\033[95m{text}\033[0m"

# Demonstrate each color function
print("Color Function Demo:")
print(blue_text("This is blue text"))
print(red_text("This is red text"))
print(green_text("This is green text"))
print(yellow_text("This is yellow text"))
print(purple_text("This is purple text"))

# Create color selection menu
print("\nAvailable colors:")
print("1. Blue")
print("2. Red")
print("3. Green")
print("4. Yellow")
print("5. Purple")

# Get user input
color_choice = input("\nChoose a color (1-5): ")
text = input("Enter the text you want to display: ")

# Process user input and display colored text
if color_choice == "1":
    print(blue_text(text))
elif color_choice == "2":
    print(red_text(text))
elif color_choice == "3":
    print(green_text(text))
elif color_choice == "4":
    print(yellow_text(text))
elif color_choice == "5":
    print(purple_text(text))
else:
    print("Invalid color choice!")