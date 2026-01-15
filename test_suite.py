import sys
import os

# Ensure we can import modules from the current directory
sys.path.append(os.getcwd())

from modules.result import result
from modules.comp_op import PI

def run_test(expression_list, expected_value, tolerance=1e-5):
    """
    Runs a single test case.
    
    Args:
        expression_list (list): The input list for the result function.
        expected_value (float or bool): The expected result.
        tolerance (float): Tolerance for floating point comparisons.
    """
    print(f"Testing: {expression_list}", end=" ... ")
    
    # Capture stdout to avoid clutter
    from io import StringIO
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        # Create a copy of the list because result() modifies it in place
        res_list = result(expression_list[:])
        
        actual_value = res_list[0] if res_list else False
    except Exception as e:
        actual_value = False
    finally:
        sys.stdout = old_stdout

    if expected_value is False:
        if actual_value is False:
            print("PASS")
            return True
        else:
            print(f"FAIL (Expected False, got {actual_value})")
            return False

    if actual_value is False:
        print(f"FAIL (Expected {expected_value}, got False/Error)")
        return False

    try:
        if abs(actual_value - expected_value) < tolerance:
            print("PASS")
            return True
        else:
            print(f"FAIL (Expected {expected_value}, got {actual_value})")
            return False
    except:
        print(f"FAIL (Error comparing {actual_value} and {expected_value})")
        return False

def main():
    print("Starting Test Suite...\n")
    
    tests = [
        # Basic Arithmetic
        ([1, "+", 2], 3),
        ([10, "-", 4], 6),
        ([3, "*", 5], 15),
        ([20, "/", 4], 5),
        
        # Multiple Operations (Order of Operations)
        ([2, "+", 3, "*", 4], 14), # 2 + 12 = 14
        ([10, "-", 2, "*", 3], 4), # 10 - 6 = 4
        ([20, "/", 5, "+", 2], 6), # 4 + 2 = 6
        
        # Parentheses
        (["(", 2, "+", 3, ")", "*", 4], 20), # 5 * 4 = 20
        ([2, "*", "(", 3, "+", 4, ")"], 14), # 2 * 7 = 14
        (["(", 1, "+", 2, ")", "*", "(", 3, "+", 4, ")"], 21), # 3 * 7 = 21
        (["(", "(", 1, "+", 2, ")", "*", 2, ")"], 6), # (3 * 2) = 6
        
        # Trigonometry (Values depend on comp_op implementation)
        # Assuming comp_op.sin/cos/tan take radians, but user inputs degrees handled by 'rad'
        (["sin", 0], 0),
        (["cos", 0], 1),
        (["tan", 45], 1), # tan(45) approx 1
        
        # Percent
        ([100, "percent", 10], 10), # 10% of 100
        ([50, "+", 100, "percent", 10], 60), # 50 + 10 = 60
        
        # Edge Cases / Errors
        ([10, "/", 0], False), # Division by zero
        (["sin"], False), # Missing argument
        (["+", 5], False), # Missing left operand (might be handled as 0+5 depending on logic, but main checks bounds)
        ([5, "+"], False), # Missing right operand
    ]
    
    passed = 0
    total = len(tests)
    
    for inputs, expected in tests:
        if run_test(inputs, expected):
            passed += 1
            
    print(f"\nTest Summary: {passed}/{total} tests passed.")

if __name__ == "__main__":
    main()
