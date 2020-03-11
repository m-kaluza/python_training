from model.group import Group
from model.contact import Contact
import random


def test_add_group_to_contact(app, db, json_contacts, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group2contact"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Monika", lastname="Kowal"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_group_to_contact_by_id(contact.id)

