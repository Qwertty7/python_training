# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
# фунлция без класса
def is_alert_present (wd):
    try:
        wd.switch_to_alert()
        return True
    except:
        return False

# класс - внутри методы - все на одном уровнеб эта функция вннутри класса, д.б. параметр - self
# self это  обьект которым вызывается метод
class TestAddGroup(unittest.TestCase):
    def setUp (self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group (self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout (self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page (self, wd):
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def create_group (self, wd):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("fhdjsk")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("fdkjlds")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("fldsjf")
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_group_page (self, wd):
        # open group page
        wd.find_element_by_link_text("groups").click()

    def login (self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page (self, wd):
        # open home page
        wd.get("http://localhost/addressbook/index.php")

    def tearDown (self):
        self.wd.quit()

# указывает как должен запускаться сценарий - через unittest
if __name__ == "__main__":
    unittest.main()
