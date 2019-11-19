# -*- coding: utf-8 -*-
from contact import Contact
import pytest
from appcontact import Appcontact

@pytest.fixture
def app(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.login( username="admin", password="secret")
        app.create_contact(Contact(firstname="Anna", lastname="Nowak", title="miss", mobile="692444520", email="anna@interia.pl", address="ul. Nowa 1, Katowice"))
        app.logout()


def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="", lastname="", title="", mobile="", email="", address=""))
        app.logout()
