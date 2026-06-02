correct = "python123"
attempts = 0
guess = ""

while guess != correct and attempts < 3:
    guess = input("Enter password: ")
    if guess != correct:
        attempts += 1
        if attempts < 3:
            print(f"Incorrect. {3 - attempts} attempt(s) remaining.")

if guess == correct:
    print("Access granted.")
else:
    print("Account locked. Try again later.")