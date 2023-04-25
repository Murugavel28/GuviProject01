from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains




class test_case2:
    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Chrome()
    username = "Admin"
    password = "12345"
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    

    @pytest.mark.html
    def login(self):
        self.driver.get(self.url)
        self.driver.maximize_window
        time.sleep(5)
        # For Login
        self.driver.find_element(by=By.NAME, value=self.input_box_username).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.input_box_password).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.login_xpath).click()
        time.sleep(4)
        error_msg = driver.find_element(by=By.XPATH, value=self.error_xpath).text
        assert error_msg == "Invalid credentials"
