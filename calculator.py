#!/usr/bin/env python3
"""
Simple calculator for A + B + C operation
Implementation for issue: A + B + C | start
"""

def add_three_numbers(a, b, c):
    """
    Add three numbers A + B + C
    
    Args:
        a (float): First number
        b (float): Second number  
        c (float): Third number
        
    Returns:
        float: Sum of A + B + C
    """
    return a + b + c


def main():
    """Main function for command line interface"""
    print("Calculator: A + B + C")
    print("=" * 20)
    
    try:
        # Get input from user
        a = float(input("Enter value for A: "))
        b = float(input("Enter value for B: "))
        c = float(input("Enter value for C: "))
        
        # Calculate result
        result = add_three_numbers(a, b, c)
        
        # Display result
        print(f"\nResult: {a} + {b} + {c} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except KeyboardInterrupt:
        print("\nOperation cancelled")


if __name__ == "__main__":
    main()