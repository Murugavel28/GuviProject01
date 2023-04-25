import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://orangehrm-demo-6x.orangehrmlive.com/")
    request.cls.driver = driver
    username = driver.find_element_by_id("txtUsername")
    username.send_keys("Admin")
    password = driver.find_element_by_id("txtPassword")
    password.send_keys("admin123")
    login_btn = driver.find_element_by_id("btnLogin")
    login_btn.click()
    pim_module = WebDriverWait(driver, 10).until()
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestDeleteEmployee:
    
    def test_delete_employee(self):
        driver = self.driver
        checkbox = driver.find_element_by_xpath("//td[text()='John Smith']/../td/input[@type='checkbox']")
        checkbox.click()
        delete_btn = driver.find_element_by_id("btnDelete")
        delete_btn.click()
        alert = driver.switch_to.alert
        alert.accept()
        assert "Successfully Deleted"
