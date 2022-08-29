import sys
import requests
from datetime import datetime
from formatting import format_msg


def send(name, website=None, verbose = False):
    if website==None:
        msg = format_msg(my_name=name)
    else:
        msg = format_msg(my_name=name, my_website=website)
    if verbose:
        print(name, website)
    #send message
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was un error"

# ochrana, aby sa tieto funkcie nevolali ked sa knižnica importuje ale iba ked sa vola
if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv)>1:
        name = sys.argv[1]
    response = send(name, verbose = True)
    print(response)