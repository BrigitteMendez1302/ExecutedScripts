# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt","w")
print('mendez 2 2 4')
# \n is placed to indicate EOL (End of Line)
file1.close() #to change file access modes
file1 = open("myfile.txt","r+")
print(file1.read())

file1.close()
