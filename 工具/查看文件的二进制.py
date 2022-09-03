filename = r"C:\Users\xuebin\Desktop\test"

with open(filename, "rb+") as f:
    file_data = f.read()
    print(file_data)
