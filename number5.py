'''
5. Write a progrrma to input numer and print Absolute value of that number
'''

while True:
    try:
        user_input = input("Enter a numberer (enter 0 to exit): ")

        if user_input.lower() == 'x':
            print("Exiting program.")
            break
        
        number = int(user_input)

        print(f"Absolute value of {number} is: {abs(number)}")
    except ValueError:
        print("Error: Please enter a valid integer.")