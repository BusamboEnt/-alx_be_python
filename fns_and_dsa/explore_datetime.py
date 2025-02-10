
import datetime

def display_current_datetime():
   
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")


def calculate_future_date():
    
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.date.today()  # Use date.today() for only the date part
        future_date = current_date + datetime.timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()