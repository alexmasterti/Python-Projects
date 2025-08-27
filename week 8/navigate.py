def read_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File not found.")
        return []

def navigate_file(filename):
    lines = read_lines(filename)
    if not lines:
        return

    num_lines = len(lines)
    while True:
        print(f"\nThe file '{filename}' has {num_lines} lines.")
        choice = input("Enter the line number (1 to {}), or 0 to quit: ".format(num_lines))

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice.isdigit():
            line_num = int(choice)
            if 1 <= line_num <= num_lines:
                print("Line {}: {}".format(line_num, lines[line_num - 1].strip()))
            else:
                print("Invalid line number. Please enter a number between 1 and {}.".format(num_lines))
        else:
            print("Invalid input. Please enter a valid line number or 0 to quit.")

def main():
    filename = input("Enter the filename: ")
    navigate_file(filename)

if __name__ == "__main__":
    main()
