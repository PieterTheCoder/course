# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

"""r stands for read-only. a stands for append. w stands for write"""
# with open("my_file.txt", mode="a") as file:
#     contents = file.write("\nHello world")
#     print(contents)

"""Absolute path"""
# with open("/home/ep/Desktop/my_file.txt") as file:
#     """generate a new file if the mode was write and you name a file that doesn't exit from scratch"""
#     contents = file.read()
#     print(contents)

"""Relative path"""
with open("../../Desktop/my_file.txt") as file:
    """generate a new file if the mode was write and you name a file that doesn't exit from scratch"""
    contents = file.read()
    print(contents)