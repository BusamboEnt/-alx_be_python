def daily_reminder():

  task = input("What is your task for today? ")
    priority = input("What is the priority of this task (high, medium, low)? ").lower()
    time_bound = input("Is this task time-bound (yes or no)? ").lower()

match priority:
        case "high":
          reminder = f"Your high priority task: '{task}'. "
        case "medium":
          reminder = f"Your medium priority task: '{task}'. "
        case "low":
          reminder = f"Your low priority task: '{task}'. "
        case _:
           reminder = "Invalid priority. Please check your priority."

    if time_bound == "yes":
        reminder += "That requires immediate attention today!"
    
    if "Invalid priority" not in reminder:
        print(reminder)

if __name__ == "__main__":
    daily_reminder()
