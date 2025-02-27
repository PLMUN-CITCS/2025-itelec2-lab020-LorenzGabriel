def get_integer_input():
    """
    Handles user input to obtain an integer.
    
    Returns:
        int: The integer input by the user.
    """
    while True:
        try:
            # Prompt the user to enter an integer
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    """
    Determines if a given number is even or odd.
    
    Args:
        number (int): The number to be checked.
        
    Returns:
        str: A message indicating whether the number is "Even" or "Odd".
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    # Get the integer input from the user
    number = get_integer_input()
    
    # Determine if the number is even or odd and display the result
    result = check_even_odd(number)
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
