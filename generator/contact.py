from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", title="", mobile="", home="", work="", secondaryphone="", email="",
                    address="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10), title=random_string("title", 3),
            mobile=random_string("mobile", 9), home=random_string("home", 9), work=random_string("work", 9),
            secondaryphone=random_string("secondaryphone", 9), email=random_string("email", 10),
            address=random_string("address", 15), email2=random_string("email2", 15), email3=random_string("email3", 15))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))