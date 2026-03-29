# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="a") as file:
    """r stands for read-only. a stands for append. w stands for write"""
    contents = file.write("\nHello world")
    print(contents)

with open("new_file.txt", mode="w") as file:
    """generate a new file if the mode was write and you name a file that doesn't exit from scratch"""
    file.write("Hello world")