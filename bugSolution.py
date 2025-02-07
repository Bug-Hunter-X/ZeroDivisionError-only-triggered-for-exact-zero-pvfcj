def function_with_uncommon_error_solution(a, b):
    if abs(a) < 1e-9: # Check if a is close to zero
        raise ZeroDivisionError("Division by zero or near zero")
    elif a > 10:
        return a + b
    else:
        return a - b

result = function_with_uncommon_error_solution(0,5) # will raise ZeroDivisionError
print(result)