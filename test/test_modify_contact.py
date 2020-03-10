from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Monika", lastname="Kowal"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact_data = Contact(firstname="Joanna", lastname="Nowakowska", title="mrs", mobile="604153233", home="326305050",
                      work="326502021", secondaryphone="664661660", email="joanna@interia.pl",
                      address="ul. Międzyblokowa 11, Katowice")
    app.contact.modify_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

