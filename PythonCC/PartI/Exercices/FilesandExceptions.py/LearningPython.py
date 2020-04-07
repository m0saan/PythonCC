# with open("learning_python.txt") as object_file:
#     contents = object_file.read()

# print(contents)

# with open("learning_python.txt") as object_file:
#     for line in object_file:
#         print(line.strip())

with open("learning_python.txt") as object_file:
    content_list = object_file.readlines()

for item in content_list:
    print("Yes " + item.strip())
