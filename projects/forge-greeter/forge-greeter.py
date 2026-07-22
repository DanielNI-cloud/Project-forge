print("Welcome to Project Forge!")
def ask_validated(question,min_length=2):
    answer = ""

    while not answer or len(answer) < min_length:
        answer = input(question).strip()

    return answer

def ask_validated_num(question,min_length=1,numbers_only=True):
    reply = ""

    while not reply or len(reply) < min_length:
        reply = input(question).strip()

    if numbers_only and not reply.isdigit():
        print("Please enter a valid number.")
        return ask_validated_num(question, min_length, numbers_only)

    return reply


name = ask_validated("What is your name? ")
print(f"Hello, {name}! Let's build something amazing together.")

age = ask_validated_num("May I ask your age? ")
idea = ask_validated("What is your idea? ")

reason = ask_validated(f"Why do you want to build {idea}? ")

print(f"That's a fantastic, {name}! Let's make it happen.")
print()
print(f"Great, {name}!")
print(f"You want to build: {idea}")
print(f"Your reason is: {reason}")
print("Let's get started.")
print("Let's break down the steps needed to bring your idea to life.")

first_step = ask_validated("What is the first step we should take? ")
print(f"Excellent! The first step is: {first_step}")