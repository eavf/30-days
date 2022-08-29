import os
import datetime
import uuid


BASE_DIR = os.path.dirname(__file__)
log_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)
print ("I am in logger")

def trigger_log_save():
    # current dateTime
    now = datetime.datetime.now()
    uniqstr = uuid.uuid4().hex[:6]

    # convert to string
    date_time_str = now.strftime("-%Y-%m-%d-%H")
    nnam = uniqstr + date_time_str
    filename = f"{nnam}.txt"
    filepath = os.path.join(log_dir, filename)
    with open(filepath, 'w+') as f:
        f.write(str(now))