import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield
    driver.close()

def test_edit_existing_employee(setup):
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    driver.find_element_by_id("menu_pim_viewPimModule").click()
    driver.find_element_by_id("empsearch_employee_name_empName").send_keys("Murugavel")
    driver.find_element_by_id("searchBtn").click()
    driver.find_element_by_css_selector("a[href*='empNumber=1234']").click()
    driver.find_element_by_id("personal_txtEmpFirstName").clear()
    driver.find_element_by_id("personal_txtEmpFirstName").send_keys("Murugavel")
    driver.find_element_by_id("personal_txtEmpLastName").clear()
    driver.find_element_by_id("personal_txtEmpLastName").send_keys("R")
    driver.find_element_by_id("btnSave").click()
    success_msg = driver.find_element_by_css_selector(".message.success").text
    assert success_msg == "Successfully Saved"
