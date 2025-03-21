def draw_pyramid(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)

# Call function
draw_pyramid(9)