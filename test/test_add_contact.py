# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.appcontact import Appcontact


@pytest.fixture
def app(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.contact_creation(Contact(first_name="Elena", last_name="Talley", address="Moscow", email="g345@gmail.com"))
    app.logout()


def test_add_empty_contact (app):
    app.login(username="admin", password="secret")
    app.contact_creation(Contact(first_name="", last_name="", address="", email=""))
    app.logout()


def test_add_contact_with_empty_address_and_email(app):
    app.login(username="admin", password="secret")
    app.contact_creation(Contact(first_name="Petr", last_name="Ivanov", address="", email=""))
    app.logout()




    





