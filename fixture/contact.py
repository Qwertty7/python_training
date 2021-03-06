from model import contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
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
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contact_page()

    def delete_first_contact(self):
        wd = self.app.wd
    #     select first contact
        wd.find_element_by_name("selected[]").click()
    #   wd.find_element_by_id("13").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm delete contact popup window
        wd.switch_to_alert().accept()


    def delete_all_contacts(self):
        wd = self.app.wd
    #     select first contact
        wd.find_element_by_id("MassCB").click()
    #   wd.find_element_by_id("13").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm delete contact popup window
        wd.switch_to_alert().accept()


    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()