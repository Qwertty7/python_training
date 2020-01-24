

def test_print_all_groups(app):
    app.session.login(user="admin", password="secret")
    app.group.print_all_groups()
    app.session.logout()