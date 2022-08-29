import os


this_file_path = os.path.abspath(__file__)
print (this_file_path)

BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
print (BASE_DIR, ENTIRE_PROJECT_DIR)

#email_txt = os.path.join("templates", "email.txt") 

email_txt = os.path.join(BASE_DIR, "templates", "email.txt")      # relative path to this file


content = ""

with open(email_txt, "r") as f:
    content = f.read()

print(content.format(name = "Justin"))