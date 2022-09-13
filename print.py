# Print to the text file
file = open('log.txt', 'w')
print('This is a sample print male', file = file)
file.close()

file1 = open("log.txt","r+")
str_file1 =  file1.read()
str_file = str_file1.split()
print(str_file)
file1.close()

if 'male' in str_file:
    print("success")