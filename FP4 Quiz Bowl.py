import random

# Dictionary of questions and answers
questions = {
    "What planet is known as the Red Planet?": "mars",
    "What is the largest mammal in the world?": "blue whale",
    "What is the capital city of Japan?": "tokyo",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the chemical symbol for gold?": "au"
}

# Welcome message
print("Welcome to the Trivia Quiz!")
print("Type your answers below each question.\n")

# Initialize score
score = 0

# Convert dictionary items to list and shuffle them
question_list = list(questions.items())
random.shuffle(question_list)

# Loop through each question
for question, correct_answer in question_list:
    # Display question and get answer
    print(question)
    user_answer = input("Your answer: ").lower()
    
    # Check answer and provide feedback
    if user_answer == correct_answer:
        print("Correct! Well done!\n")
        score += 1
    else:
        print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}\n")

# Calculate percentage
percentage = (score / len(questions)) * 100

# Display final score
print("Quiz Complete!")
print(f"Your final score: {score} out of {len(questions)}")
print(f"Percentage: {percentage}%")