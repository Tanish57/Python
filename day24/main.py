# file = open("my_file.txt")
# with the method above you always have to remember to close the file with file.close() but with the method below you can
# do whatever you wanted to and don't even need to call the close function, with method closes it by default after inclination

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="a") as file:     # a stands for append, r for read, and w for write
    file.write("\nNew text.")

with open("new_file.txt", mode="w") as newfile:
    newfile.write("Hello World!")

