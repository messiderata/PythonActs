'''
6. Write a program to input any number and check it is positive or negative number
'''
while True:
    try:
        user_input = input("Enter a number (enter 0 to exit): ")

        if user_input.lower() == 'x':
            print("Exiting program.")
            break
        
        number = float(user_input)

        if (number > 0):
            print(f"{number} is a positive number ")
        elif (number < 0):
            print(f"{number} is a negative number ")
        else:
            print(f"{number} is 0")
 
    except ValueError:
        print("Error: Please enter a valid integer.")