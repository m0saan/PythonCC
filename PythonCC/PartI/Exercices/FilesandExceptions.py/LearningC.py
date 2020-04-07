with open("learning_python.txt") as object_file:
    content = object_file.readlines()

for item in content:
    s = item.replace("Python", "C++")
    print(s.strip())
