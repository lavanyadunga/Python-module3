print("Welcome,Please enter your age")
age=input()
try:
    age = int(age)
    if age < 18:
        print("Access denied..you too young!")
    elif age in range(18, 21):
        print("You can come in,but not drinking")
    else:
        print("Welcome ,enjoy the club")
except ValueError:
    print("Error: Please enter a valid integer for age")