def unique_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
        unique_words = sorted(set(words))
        for word in unique_words:
            print(word)
    except FileNotFoundError:
        print("File not found.")

def main():
    filename = input("Enter the filename: ")
    unique_words(filename)

if __name__ == "__main__":
    main()
