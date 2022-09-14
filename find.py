def find_word_in_print():
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

def get_sys():
    original_stdout = sys.stdout 

    # Create or open an existing file in write mode
    with open('log.txt', 'w') as file:
        # Set the stdout to file object
        sys.stdout = file
        print('File Mode: Print text to a file. bru')
        
        # Set the stdout back to the original or default mode
        sys.stdout = original_stdout

    with open('log.txt', 'r') as reader:
        # Read & print the entire file
        printed_text = reader.read()
        str_file = printed_text.split()
        if 'male' in str_file:
            return 1
        elif 'female' in str_file:
            return 0
        print(printed_text)