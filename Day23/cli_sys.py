import sys

if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except:
        name = input ('What is your name?\n')
    from getpass import getpass
    pw = getpass ('What is your password?\n')
    
    print (name, pw)
