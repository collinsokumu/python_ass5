try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Adding some numbers: 1, 2, 3\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("Another appended line.\n")
        file.write("One more appended line.\n")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Task completed.")
