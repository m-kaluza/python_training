from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Monika", lastname="Kowal"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Joanna", lastname="Nowakowska", title="mrs", mobile="604153233", home="326305050",
                      work="326502021", secondaryphone="664661660", email="joanna@interia.pl",
                      address="ul. Międzyblokowa 11, Katowice")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

