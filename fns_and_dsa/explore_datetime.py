import datetime

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """Calculates and displays the future date after adding a specified number of days."""
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
        return  # Exit the function if the input is invalid

    current_date = datetime.datetime.now().date()  # Get only the date part
    future_date = current_date + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date()
