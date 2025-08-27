def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print("No")
                print(f"Difference found:\n{file1}: {line1.strip()}\n{file2}: {line2.strip()}")
                return
    print("Yes")

def main():
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    compare_files(file1, file2)

if __name__ == "__main__":
    main()
