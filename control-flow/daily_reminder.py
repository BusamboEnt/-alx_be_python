def main():
    
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    
    match priority:
        case "high":
            message = f"'{task}' is a high priority task."
        case "medium":
            message = f"'{task}' is a medium priority task. Don't forget to complete it."
        case "low":
            message = f"'{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            message = "Invalid priority entered. Defaulting to low priority."
    
    
    if time_bound == "yes":
        message += " That requires immediate attention today!"
    
    
    print("\nReminder:", message)

if __name__ == "__main__":
    main()
