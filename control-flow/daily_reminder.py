def main():

    test_cases = [
        ("Finish project report", "high", "yes"),
        ("Read a book", "low", "no"),
        ("Submit assignment", "medium", "yes"),
        ("Exercise", "high", "no"),
        ("Call a friend", "low", "yes"),
        ("Reply to emails", "medium", "no"),
    ]
    
    for task, priority, time_bound in test_cases:
       
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
        
        
        print(f"\nReminder: {message}")

if __name__ == "__main__":
    main()
