''' 
3. Write a program enter monthly salte of Salesman and give him commision i.e if 
the monthly sale is more than 500000 then commisionwill be 10% of monthly sale otherwise 5%

'''

def calculate_commission(monthly_sales):
    if monthly_sales > 5000000:
        commission = 0.10 * monthly_sales
    else:
        commission = 0.05 * monthly_sales
    return commission


while True:
    try:
        user_input = input("Enter your monthly sales (or 'x' to exit): ")

        if user_input.lower() == 'x':
            print("Exiting program.")
            break

        monthly_sales = float(user_input)

        if monthly_sales < 0 :
            print("Error: Please enter a positive number.")
            continue

        commission = calculate_commission(monthly_sales)
        print(f"The commission for the monthly sales of {monthly_sales} is {commission}")

    except ValueError:
        print("Error: Enter valid value.")

