def print_rectangle(count_r, count_c):
    for r in range(count_r):
        for c in range(count_c):
            print("*", end="")
        print()


print_rectangle(5, 5)


def print_rectangle(height, width, fill_char, end_char):
    for r in range(height):
        for c in range(width):
            print(fill_char, end=end_char)
        print()


print_rectangle(3, 5, "x", "")
