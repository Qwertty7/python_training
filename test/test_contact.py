# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.create(Contact(first_name="Elena", last_name="Talley", address="Moscow", email="g345@gmail.com"))
    app.session.logout()


def test_add_empty_contact (app):
    app.session.login(user="admin", password="secret")
    app.contact.create(Contact(first_name="", last_name="", address="", email=""))
    app.session.logout()


def test_add_contact_with_empty_address_and_email(app):
    app.session.login(user="admin", password="secret")
    app.contact.create(Contact(first_name="Petr", last_name="Ivanov", address="", email=""))
    app.session.logout()










