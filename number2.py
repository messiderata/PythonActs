# 2. Write a program to enter any age and check it is teenaer or not

teenage_min_age = 13
teenage_max_age = 19

while True:
    try:
        age = int(input("Enter age (Enter 0 to exit):"))

        if age == 0:
            print("Exiting the program...")
            break
        if teenage_min_age <= age <= teenage_max_age:
            print(f"The {age} is within the teenage range.")
        else:
            print(f"The {age} is not within the teenage range.")
    except ValueError:
        print("Error: Please enter valid age.")