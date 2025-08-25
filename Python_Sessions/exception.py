# exception module for handling custom exceptions
filename = input("Enter filename: ")
books = []
try:
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            books.append(line)
except FileNotFoundError as e:
    print("could not find file named" + filename)
except OSError as e:
    print("file found - error reading file")
except Exception as e:
    print("an unexpected error occurred")
