# this is the method I used:
# f1 = open("file1.txt", "r")
# f2 = open("file2.txt", "r")
#
# l1 = [int(n) for n in f1]
# l2 = [int(n) for n in f2]

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(n) for n in file_1_data if n in file_2_data]

# Write your code above 👆

print(result)


