print("Welcome to Project Forge!")
def ask_validated(
        question,
        min_length=2, 
        numbers_only=False):
    while True:
        answer = input(question).strip()

        if len(answer) < min_length:
            print(f"Please enter at least {min_length} character(s).")
            continue

        if numbers_only and not answer.isdigit():
            print("Please enter a valid number.")
            continue

        return answer

name = ask_validated("What is your name? ")
print(f"Hello, {name}! Let's build something amazing together.")

age = ask_validated("May I ask your age? ",
                    min_length=1,
                    numbers_only=True)

idea = ask_validated("What is your idea? ")

reason = ask_validated(f"Why do you want to build {idea}? ")

print(f"That's a fantastic, {name}! Let's make it happen.")
print()
print(f"Great, {name}!")
print(f"You are {age} years old and you want to build: {idea}.")
print(f"Your reason is: {reason}")
print("Let's get started.")
print("Let's break down the steps needed to bring your idea to life.")

first_step = ask_validated("What is the first step we should take? ")
print(f"Excellent! The first step is: {first_step}")