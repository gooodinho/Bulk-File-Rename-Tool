try:
    file = open("test.txt", encoding="utf-8")
    try:
        print(file.read(3))

        # Set file_position equal 0
        file.seek(0)
        print(file.read(3))

        # Get file_position value (in bytes)
        position = file.tell()
        print(f"File position value = {position}")

        file.seek(0)
        print(file.readline(), end="")
        print(file.readline(), end="")

        file.seek(0)
        for line in file:
            print(line, end="")

        file.seek(0)
        s = file.readlines()
        print(s)
    finally:
        file.close()
except FileNotFoundError:
    print("No such file or directory")

try:
    with open("test.txt", "r", encoding="utf-8") as file:
        print(file.read(3))
except FileNotFoundError:
    print("No such file or directory")
finally:
    print(file.closed)
