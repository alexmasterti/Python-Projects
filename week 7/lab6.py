fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')
