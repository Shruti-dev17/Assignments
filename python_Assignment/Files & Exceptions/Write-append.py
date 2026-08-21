# Assignment 4 :
# Task 2:Write and Append Data to a File

# Taking user input
write_data= input("Enter text to write to the file : ")

# Writing given text into the file
with open(r"F:\Desktop\code\Assignment\Python_Assignment\Assignment 4\output.txt",'w') as fh :
    fh.write(write_data)
    print("Data successfully written to output.txt")

# Appending additional data 
append_data = input("Enter text to append in output.txt : ")
with open(r"F:\Desktop\code\Assignment\Python_Assignment\Assignment 4\output.txt",'a') as fh :
    fh.write(f"\n{append_data}")
    print("Data successfully appended.")

# Reading and displaying the final content of file
with open(r"F:\Desktop\code\Assignment\Python_Assignment\Assignment 4\output.txt",'r') as fh :
    read_file=fh.read()
    print(f"Final content of the file :\n{read_file}")
