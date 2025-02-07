def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a # ZeroDivisionError, but only if a is exactly 0
    elif a > 10:
        return a + b
    else:
        return a - b

result = function_with_uncommon_error(0,5) # will raise ZeroDivisionError
print(result)