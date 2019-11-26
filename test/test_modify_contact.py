from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Monika", lastname="Kowal"))
    app.contact.modify_first_contact(
        Contact(firstname="Joanna", lastname="Nowakowska", title="mrs", mobile="604153233", email="joanna@interia.pl",
                address="ul. Międzyblokowa 11, Katowice"))

