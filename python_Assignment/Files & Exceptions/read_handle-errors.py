# Assignment 4 : 
# Task 1 :Read a file and handle errors


# opening the file in read mode and using try-except method for handling error
try:
    fh = open(r'Python_Assignment\Assignment 4\sample.txt','r') 

except FileNotFoundError :
   print("The file sample.txt was not found")

# else is used to run code after error is validated and no error is found
else:
    read_file= fh.readlines() # using readlines() to read the content of file line by line
    count = 1 

    for line in read_file:
        print(f"line {count}: {line}")
        count+=1

    fh.close() # closing the file.

