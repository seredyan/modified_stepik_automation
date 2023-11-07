

import random
import string
import os.path
import jsonpickle
from model.users import User
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits *6
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # добавили спец символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen, 11, 199))])

def random_char_email(maxlen):
    emails = ["a@gmail.com", "b@ya.ru", "c@mail.ru", "d@icloud.com", "e@company.com", "f@yahoo.com", "g@outlook.com"]
    symbols = (''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(maxlen))))
    return (symbols + str(random.randrange(12, 199, 1)) + random.choice(emails))

# def random_digits(maxlen):
#     symbols = string.digits #+ " " * 3
#     return "".join([random.choice(symbols) for i in range(maxlen)])




testdata = [User(email=random_char_email(4), password=random_string('pswrd', 6)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# other way:   file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")
# из родительской директории перпходим выше в подкаталог data

with open(file, "w") as file_out:
    jsonpickle.set_encoder_options("json", indent=2)
    file_out.write(jsonpickle.encode(testdata))