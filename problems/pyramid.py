def star_pyramid(base_items):
    for i in range(1, base_items + 1):
        print(" " * (base_items - i), end="")
        print("* " * i)


star_pyramid(int(input("Enter the number of * in the pyramid base: ")))