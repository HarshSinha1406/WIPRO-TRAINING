# numbers_package.py

def write_numbers_to_file(filename):
    """Writes numbers 1 to 100 into a file"""
    try:
        with open(filename, "w") as f:
            for i in range(1, 101):
                f.write(str(i) + "\n")
        print("Numbers written successfully")

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")


def read_numbers_from_file(filename):
    """Reads file content safely"""
    try:
        with open(filename, "r") as f:
            print("File content:\n")
            print(f.read())

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")


# Main execution
if __name__ == "__main__":
    filename = "numbers.txt"
    write_numbers_to_file(filename)
    read_numbers_from_file(filename)
