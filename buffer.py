import sys
import io



def print_bri():
    old_stdout = sys.stdout # Memorize the default stdout stream
    print('pastor')
    sys.stdout = buffer = io.StringIO()
    sys.stdout = old_stdout # Put the old stream back in place
    
    whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
    print('bri', whatWasPrinted) # Why not to print it?


def print_bri2():
    print('mendez 2 2 4')


sys.stdout = open("test.txt", "w")
print_bri2()

file1 = open("test.txt","r+") 
file1.read()

sys.stdout.close()
