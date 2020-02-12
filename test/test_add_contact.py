# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anna", lastname="Nowak", title="miss", mobile="692444520", email="anna@interia.pl",
                      address="ul. Nowa 1, Katowice")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", title="", mobile="", email="", address=""))
