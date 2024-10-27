# Welcome message
print("Welcome to Mad Libs! Please enter the following words:\n")

# Get inputs from user
large_object = input("Enter a large object: ")
large_objects = input("Enter large objects (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
restaurant = input("Enter a restaurant: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")

# Print blank line before story
print("\nHere's your Mad Libs story:\n")

# Create and print story using f-string
print(f"""I've had a very {adjective} day.
This morning, I dropped a box of {large_objects} on my {body_part}.
Then, at lunch, I went to {restaurant} for their delicious {food1},
But the waiter brought me {food2}, which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof.""")