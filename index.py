file = open("odd_even.py", "w")

file.write(f"if x == 0:\n")
file.write(f"    return True\n")

for x in range (0, 10001):
    file.write(f"if x == {x}:\n")
    if (x % 2 == 0):
        file.write(f"    return True\n")
    else:
        file.write(f"    return False\n")

file.close()