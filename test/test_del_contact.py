from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Monika", lastname="Kowal"))
    app.contact.del_first_contact()
