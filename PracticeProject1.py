import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_ddl_originStation1_CTXT']").send_keys("Goa")
driver.find_element(By.XPATH, "//a[normalize-space()='Goa (GOI)']")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_ddl_destinationStation1_CTXT']").send_keys("Mumbai")
driver.find_element(By.XPATH, "(//a[@class='ui-state-default'][normalize-space()='30'])[1]").click()
driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_rbtnl_Trip_1']").click()
driver.find_element(By.ID, "ctl00_mainContent_view_date2").click()
driver.find_element(By.XPATH, "//a[normalize-space()='4']").click()
driver.find_element(By.ID, "divpaxinfo").click()















time.sleep(3)