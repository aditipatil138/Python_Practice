filename = input("Enter the file name with extension: ")
file_extension = filename.split(".") 
print("The Entension of the entered file is: " + repr(file_extension[-1]))