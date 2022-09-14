import sys

# Prints in a console/terminal
# Store the reference of original standard output into variable


def sys_func():
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
        print(printed_text)


def printHola():
    print('print hola')


original_stdout = sys.stdout
    # Create or open an existing file in write mode
with open('log.txt', 'w') as file:
    # Set the stdout to file object
    sys.stdout = file
    printHola()

    # Set the stdout back to the original or default mode
    sys.stdout = original_stdout

with open('log.txt', 'r') as reader:
    # Read & print the entire file
    printed_text = reader.read()
    print(printed_text)    