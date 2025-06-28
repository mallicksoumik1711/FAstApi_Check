def analyze_complexity(code_snippet: str):
    """
    Analyzes the time and space complexity of a given code snippet.
    Handles basic loops, recursion, function calls, and data structures.
    """
    # Keywords to look for
    loop_keywords = ["for", "while"]
    recursion_keywords = ["return"]
    function_call_keywords = ["def"]  # Function definition keyword
    data_structure_keywords = ["list", "dict", "set", "array", "[]", "{}"]

    # Initialize complexity
    time_complexity = "O(1)"
    space_complexity = "O(1)"

    # Split code snippet into lines for analysis
    lines = code_snippet.split("\n")
    loop_count = 0
    recursion_count = 0
    function_call_count = 0
    data_structure_count = 0

    # Analyze each line in the code snippet
    for line in lines:
        line = line.strip()

        # Check for loops
        if any(keyword in line for keyword in loop_keywords):
            loop_count += 1
            time_complexity = "O(n)"  # Assuming simple loop, adjust for nested loops later
        
        # Check for recursion
        if any(keyword in line for keyword in recursion_keywords) and "(" in line and ")" in line:
            recursion_count += 1
            time_complexity = "O(2^n)"  # Exponential recursion, adjust as needed

        # Check for function calls (if there are any)
        if any(keyword in line for keyword in function_call_keywords):
            function_call_count += 1
            time_complexity = "O(n)"  # Assumption: Single function calls can be linear

        # Check for data structures
        if any(keyword in line for keyword in data_structure_keywords):
            data_structure_count += 1
            space_complexity = "O(n)"  # Space complexity increases with data structures

    # Adjust time complexity based on loop nesting or recursion
    if loop_count > 1:
        time_complexity = "O(n^2)"  # Assuming nested loops
    elif recursion_count > 1:
        time_complexity = "O(2^n)"  # Assuming exponential recursion
    
    # Adjust space complexity for recursive calls (stack space)
    if recursion_count > 0:
        space_complexity = "O(n)"  # Stack space for recursion

    return time_complexity, space_complexity


# Example usage
code = """
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

"""

time, space = analyze_complexity(code)

print("Time Complexity:", time)
print("Space Complexity:", space)
