# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", title="", mobile="", email="", address="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5), title=random_string("title", 3),
            mobile=random_string("mobile", 9), home=random_string("home", 9),
            work=random_string("work", 9), secondaryphone=random_string("secondaryphone", 9), email=random_string("email", 7),
            email2=random_string("email2", 6), email3=random_string("email3", 6),
            address=random_string("address", 15))
    for i in range(2)

]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
# app.contact.create(Contact(firstname="", lastname="", title="", mobile="", email="", address=""))
