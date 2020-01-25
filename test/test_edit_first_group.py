

def test_edit_first_group(app):
    app.session.login(user="admin", password="secret")
    app.session.logout()
