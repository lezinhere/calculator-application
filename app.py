# app.py

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    print("Simple Calculator App")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = add(a, b)
    print(f"Result: {result}")
