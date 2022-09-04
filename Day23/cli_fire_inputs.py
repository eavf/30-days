from getpass import getpass
import fire

def hello(name='world'):
    return f"Hello {name}"

def login(name=None):
    if name == None:
        name = input ('What is your name?\n')
    pw = getpass ('What is your password?\n')
    return name, pw

if __name__ == '__main__':
    fire.Fire(login)
