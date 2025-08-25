with open("sample.txt", "a+") as f:
    f.write("\nnext line typing in read methods with append")
    f.seek(0)  # Move the cursor to the beginning of the file
    content = f.readlines()
    print(content)