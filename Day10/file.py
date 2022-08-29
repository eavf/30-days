fname = "hw.txt"
with open(fname, "w") as file_object:
    file_object.write("Hello world again")

with open(fname, "r") as f:
    print(f.read())
