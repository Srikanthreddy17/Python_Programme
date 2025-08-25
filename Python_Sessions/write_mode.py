f_obj = open('testing.txt', 'w' )
f_obj.write('writing in the file\nnon exist by creating with write function')
f_obj =open("testing.txt", "r")
content = f_obj.read()
print(content)
f_obj.close