import string
import os

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def extract_words(line):
    words = line.strip().split()
    return [word.translate(str.maketrans('', '', string.punctuation)).lower() for word in words]

def generate_concordance(lines):
    concordance = {}
    for line in lines:
        words = extract_words(line)
        for word in words:
            concordance[word] = concordance.get(word, 0) + 1
    return concordance

def display_concordance(concordance):
    for word, frequency in sorted(concordance.items()):
        print(f"{word}: {frequency}")

def main():
    file_name = input("Enter the name of the file: ")
    lines = read_file(file_name)
    concordance = generate_concordance(lines)
    print("Concordance (unique words and their frequencies):")
    display_concordance(concordance)

if __name__ == "__main__":
    current_directory = os.getcwd()
    print("Current directory:", current_directory)    
    main()
