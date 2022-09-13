# Program to show various ways to read and
# write data in a file.
# file1 = open("myfile.txt","w")
# \n is placed to indicate EOL (End of Line)
file1 = open("myfile.txt","r+")
str_file = file1.read()
str_file = str_file.split()
print(str_file)
file1.close()
