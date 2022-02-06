try:
    # "a+"
    file = open("out.txt", "w")

    try:
        # file.write("Hello1\n")
        # file.write("Hello2\n")
        # file.write("Hello3\n")
        # file.seek(0)
        # print(file.read())

        file.writelines(['Hello123\n', 'Hello321'])

    finally:
        file.close()

except FileNotFoundError:
    print("No such file or directory")