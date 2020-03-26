from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname>, <address>, <home>, <mobile>, <work> and <email>')
def new_contact(firstname, lastname, address, home, mobile, work, email):
    return Contact(firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work,
                   email=email)


@when('I add the contact to the list')
def add_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Monika", lastname="Kowal"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.del_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_group_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)
