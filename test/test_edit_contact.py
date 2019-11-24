from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact(
        Contact(firstname="Joanna", lastname="Nowakowska", title="mrs", mobile="604153233", email="joanna@interia.pl",
                address="ul. Międzyblokowa 11, Katowice"))
