# name = input("Enter your name: ")

# file = open("name.txt", "w")
# file.write(name)
# file.close()

# print("Name saved successfully.")


#USING FUNCTION
def FileOpener(name):
    file = open("name.txt", "w")
    file.write(name)
    file.close()
    print("Name saved successfully.")

name = input("Enter your name: ")
FileOpener(name)