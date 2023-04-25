from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains



class TC_PIM_01:
    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Chrome()
    username = "Admin"
    password = "12345"
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    pim_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'

 
    @pytest.mark.html
    def test_add_new_employee(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        action = ActionChains(self.driver)
        self.driver.find_element(by=By.NAME, value=self.input_box_username).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.input_box_password).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.login_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.pim_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.add_xpath).click()
        self.driver.find_element_by_id("firstName").send_keys("Murugavel")
        self.driver.find_element_by_id("lastName").send_keys("R")
        self.driver.find_element_by_id("employeeId").clear()
        self.driver.find_element_by_id("employeeId").send_keys("1234")
        self.driver.find_element_by_id("btnSave").click()
        assert success_msg == "Successfully Saved"
