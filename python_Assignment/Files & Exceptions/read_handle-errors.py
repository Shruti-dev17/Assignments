# Assignment 4 : 
# Task 1 :Read a file and handle errors


# opening the file in read mode and using try-except method for handling error
try:
    with open(r'F:\Desktop\code\Assignment\python_Assignment\Files & Exceptions\sample.txt','r') as fh:
        read_file= fh.readlines() # using readlines() to read the content of file line by line
        count = 1 
        
        for line in read_file:
            print(f"line {count}: {line}")
            count+=1
        
        fh.close() # closing the file.
        

except FileNotFoundError :
   print("The file sample.txt was not found")


    
