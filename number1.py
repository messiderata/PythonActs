#1.Write a program to enter any number and check it even or odd


while True:
    try:
        number = int(input("Enter a number (enter 0 to exit):"))

        if number == 0:
            print(" ")
            print("Exiting the program...")
            break
        
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")
