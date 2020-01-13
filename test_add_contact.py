# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        # change var name from driver to wd (use refactor-rename)
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(40)

    # method: test add group
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.contact_creation(wd, Contact(first_name="Elena", last_name="Talley", address="Moscow", email="g345@gmail.com"))
        self.return_to_contact_page(wd)
        self.logout(wd)


    def test_add_empty_contact (self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.contact_creation(wd, Contact(first_name="", last_name="", address="", email=""))
        self.return_to_contact_page(wd)
        self.logout(wd)


    def test_add_contact_with_empty_address_and_email(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.contact_creation(wd, Contact(first_name="Petr", last_name="Ivanov", address="", email=""))
        self.return_to_contact_page(wd)
        self.logout(wd)

    def logout (self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_contact_page (self, wd):
        wd.find_element_by_link_text("home page").click()

    def contact_creation (self, wd, contact):
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact's form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("theform").click()
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login (self, wd, username, password):
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page (self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
