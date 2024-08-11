def print_custom_pyramid(n):
    if n < 1:
        print("Enter a positive number greater than or equal to 1")
        return
    
    initial_lines = n + 1

    # Print the pyramid with only borders for the first `initial_lines - 1` lines
    for i in range(initial_lines):
        for j in range(initial_lines - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i:
                print("*", end="")
            elif i == initial_lines - 1 and k == i:
                print(n, end="")
            else:
                print(" ", end="")
        print()

    # Print the downward pyramid lines with borders
    for i in range(1, n):
        for j in range(i):
            print(" ", end="")
        for k in range(2 * (n - i) + 1):
            if k == 0 or k == 2 * (n - i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
     
    #Print the lines filled with stars below the pyramid
    stars = 5 + 2 * (n - 1)
    for m in range(n):
        print("*" * stars)

print_custom_pyramid(0)
print_custom_pyramid(1)
print_custom_pyramid(2)
print_custom_pyramid(3)

