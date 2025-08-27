def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as f_source:
            data = f_source.read()
        with open(destination_file, 'w') as f_destination:
            f_destination.write(data)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found. Please make sure you enter valid file names.")

def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")

    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
