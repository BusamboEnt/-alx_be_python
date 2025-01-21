while True:
    try:
        pattern_size = int(input("Enter the size of the pattern: "))
        if pattern_size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


row_count = 0

while row_count < pattern_size:
  for _ in range(pattern_size):
        print("*", end="")

    
  print()

  row_count += 1
