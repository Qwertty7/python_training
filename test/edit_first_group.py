

def test_edit_first_group(app):
    app.session.login(user="admin", password="secret")
    app.group.edit_first_group()
    app.session.logout()
