# robust_division_calculator.py
def safe_divide(numerator, denominator):
  
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e: # catch other potential errors.
        return f"An unexpected error occurred: {e}"