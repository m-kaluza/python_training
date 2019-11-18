# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver, username, password):
        self.open_home_page(driver)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, driver, contact):
        # init contact creation
        driver.find_element_by_link_text("add new").click()
        # fill contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        # submit contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_contact(driver, Contact(firstname="Anna", lastname="Nowak", title="miss", mobile="692444520", email="anna@interia.pl", address="ul. Nowa 1, Katowice"))
        self.logout(driver)

    def test_add_empty_contact(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_contact(driver, Contact(firstname="", lastname="", title="", mobile="", email="", address=""))
        self.logout(driver)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
