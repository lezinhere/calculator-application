# app.py

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract second number from first and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide first number by second and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """Main function that runs the calculator."""
    print("Simple Calculator App")
    print("Available operations: add, subtract, multiply, divide")
    
    # Get numbers from user
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (add/subtract/multiply/divide): ").lower().strip()
        
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            print("Invalid operation! Please use: add, subtract, multiply, or divide")
            return
        
        print(f"Result: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
