import sys
original_stdout = sys.stdout # Save a reference to the original standard output
with open('filename.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('This message will be written to a bri.')
    sys.stdout = original_stdout # Reset the standard output to its original value
