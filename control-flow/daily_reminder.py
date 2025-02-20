
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
        else:
            reminder += " Please complete it soon."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
        if time_bound == "yes":
            reminder += " It should be addressed today."
        else:
            reminder += " Consider completing it when you have time."
    case "low":
        reminder = f"'{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " You might want to get it done today."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Provide a Customized Reminder
print(reminder)
