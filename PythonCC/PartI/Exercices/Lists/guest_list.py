guest_list = ["Qajjam", "Elahrach", "Flitox"]

for item in guest_list:
    print(item)
print("-----------------------")

print(guest_list[1] + " Cannot come!")
guest_list[1] = "Pirate"
print("-----------------------")

for item in guest_list:
    print(item)
print("-----------------------")

print("I found a bigger dinner table .")
guest_list.insert(0, "Saddoun")
guest_list.insert(2, "Thahma")
guest_list.insert(5, "Ayoub")


for item in guest_list:
    print("Welcome " + item)
print("-----------------------")

print("Guys I can invite only two people for dinner .")
print("-----------------------")

for index in range(len(guest_list) - 2):
    popped_name = guest_list.pop()
    print(f"I am sorry {popped_name} but I can’t invite you to dinner.")

print(guest_list[0] + " You’re still invited.")
print(guest_list[1] + " You’re still invited.")

del guest_list[0]
del guest_list[0]
print(guest_list)
