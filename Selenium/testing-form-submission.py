from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationintesting.online/")

new_title = "Website under Automation - Idris Vohra"

console = driver.execute_script(f"document.title = '{new_title}'")
name = "Idris"
email = "idris@gmail.com"
phone = "1234561111111"
subject = "Issuing an Inquiry"
msg = "Lol, SOme DescRiptIon"

# element_to_scroll_to = driver.find_element("id", 'name')
# driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)

driver.find_element("id", "name").send_keys(name)
driver.find_element("id", "email").send_keys(email)
driver.find_element("id", "phone").send_keys(phone)
driver.find_element("id", "subject").send_keys(subject)
driver.find_element("id", "description").send_keys(msg)
driver.find_element(By.ID, "submitContact").click()
