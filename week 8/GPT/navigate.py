def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def navigate():
    filename = input("Enter the filename: ")
    lines = read_file(filename)
    num_lines = len(lines)
    while True:
        print("Number of lines in the file:", num_lines)
        line_number = int(input("Enter a line number (0 to quit): "))
        if line_number == 0:
            break
        elif 1 <= line_number <= num_lines:
            print(lines[line_number - 1])
        else:
            print("Invalid line number. Please enter a number between 1 and", num_lines)

if __name__ == "__main__":
    navigate()
