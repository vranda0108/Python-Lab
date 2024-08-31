def custom_slice(sequence, slicing_parameter):
    # Unpack the slicing parameters
    start, end, step = slicing_parameter

    # Handle default values for start, end, and step
    if start is None:
        start = 0
    if end is None:
        end = len(sequence)
    if step is None:
        step = 1

    # Handle negative indices
    if start < 0:
        start += len(sequence)
    if end < 0:
        end += len(sequence)
    
    # Create a result using list comprehension and range
    result = [sequence[i] for i in range(start, end, step)]

    # Return the result in the same type as the input sequence
    if isinstance(sequence, str):
        return ''.join(result)
    elif isinstance(sequence, tuple):
        return tuple(result)
    else:  # For lists
        return result

# Test cases
print(custom_slice([1, 2, 3, 4, 5], [1, 4, 1]))          # Output: [2, 3, 4]
print(custom_slice("Hello, World!", [7, 12, 1]))         # Output: "World"
print(custom_slice((0, 1, 2, 3, 4, 5), [5, 1, -2]))   # Output: (5, 3, 1)
print(custom_slice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [-3, -8, -2]))  # Output: [7, 5, 3]

