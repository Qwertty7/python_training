# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="fhdjsk", header="fdkjlds", footer="fldsjf"))
    app.session.logout()

def test_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()