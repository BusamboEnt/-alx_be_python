task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = ""  # Initialize reminder_message

match priority:
    case "high":
        priority_message = "high priority task"
        reminder_message = f"Reminder: '{task}' is a {priority_message}."
    case "medium":
        priority_message = "medium priority task"
        reminder_message = f"Reminder: '{task}' is a {priority_message}."
    case "low":
        priority_message = "low priority task"
        reminder_message = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."
    case _:
        priority_message = "task with undefined priority"
        reminder_message = f"Reminder: '{task}' is a {priority_message}. Please specify the priority next time."

if time_bound == "yes":
    reminder_message = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
elif priority != "low":
    reminder_message = f"Reminder: '{task}' is a {priority_message}. Consider completing it when you have time."

print(reminder_message)
