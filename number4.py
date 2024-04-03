'''
4. Write a program input any year and check it is Leap Year or Not
'''

isLeapyear = False


def leap_year_checker(year):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        isLeapyear = True
    else:
        isLeapyear = False
    return isLeapyear

def main():
    while True:
        try:
            user_input = input("Enter a year (or 'x' to exit): ")

            if user_input.lower() == 'x':
                print("Exiting program.")
                break
            
            year = int(user_input)
            if leap_year_checker(year):
                 print(f"{year} is a leap year.")
            else:
                 print(f"{year} is not a leap year.")

        except ValueError:
            print("Error: Enter valid year")

if __name__ == "__main__":
    main()