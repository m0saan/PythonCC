from Admin import Privileges, Admin

list__of__privilages = ["can add post", "can delete post", "can ban user", ]
admin = Admin(list__of__privilages)
admin.describe_user()
admin.privilege.show_privileges()
