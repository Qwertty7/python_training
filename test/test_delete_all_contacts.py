

def test_delete_first_contacts(app):
    app.session.login(user="admin", password="secret")
    app.contact.delete_all_contacts()
    app.session.logout()