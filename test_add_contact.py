# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        # change var name from driver to wd (use refactor-rename)
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(40)

    # method: test add group
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.contact_creation(wd)
        self.return_to_contact_page(wd)
        self.logout(wd)

    def logout (self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_contact_page (self, wd):
        wd.find_element_by_link_text("home page").click()

    def contact_creation (self, wd):
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact's form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Elena")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Talley")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Moscow")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("g345@gmail.com")
        wd.find_element_by_name("theform").click()
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login (self, wd):
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
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
