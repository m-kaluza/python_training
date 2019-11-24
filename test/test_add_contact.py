# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(firstname="Anna", lastname="Nowak", title="miss", mobile="692444520", email="anna@interia.pl",
                address="ul. Nowa 1, Katowice"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", title="", mobile="", email="", address=""))
