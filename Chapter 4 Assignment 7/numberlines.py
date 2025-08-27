def number_lines(input_file, output_file):
    with open(input_file, 'r') as f_input:
        lines = f_input.readlines()
    
    with open(output_file, 'w') as f_output:
        for i, line in enumerate(lines, start=1):
            f_output.write(f"{i:>4}> {line}")

def main():
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")

    number_lines(input_file, output_file)
    print(f"Program listing created in '{output_file}'.")

if __name__ == "__main__":
    main()
