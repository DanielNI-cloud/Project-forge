print("Welcome to Project Forge!")

name = ""
while not name:
    name = input("What is your name? ").strip()

print(f"Hello, {name}! Let's build something amazing together.")

idea = ""
while not idea:
    idea = input("What is your idea? ").strip()

reason = ""
while not reason:
    reason = input(f"Why do you want to build {idea}? ").strip()
    print(f"That's a fantastic, {name}! Let's make it happen.")
    
print()
print(f"Great, {name}!")
print(f"You want to build: {idea}")
print(f"Your reason is: {reason}")
print(f"Your first step is: {first_step}")
print("Let's get started.")
print("Let's break down the steps needed to bring your idea to life.")

first_step = ""
while not first_step:
    first_step = input("What is the first step we should take? ").strip()

