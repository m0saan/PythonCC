current_users = ["alice00", "betty_cooper",
                 "jug99", "admin", "hussain", "gazorpazorp"]
new_users = ["david__", "jug99", "Zuck@zuckk", "ADMIn", "fp_jones"]
if new_users:
    for n_user in new_users:
        if n_user.lower() in current_users:
            print("You need to enter a new username, the current is already in ues")
        else:
            print("The entred username is availible")
