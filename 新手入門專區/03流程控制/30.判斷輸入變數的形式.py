def determine_type(input_value):
    try:
        int(input_value)
        if '.' not in input_value:
            return "int"
    except ValueError:
        pass
    
    try:
        float(input_value)
        if '.' in input_value:
            return "float"
    except ValueError:
        pass
    
    if len(input_value) == 1 and not input_value.isdigit():
        return "char"
    
    return "string"

input_value = input().strip()
print(determine_type(input_value))