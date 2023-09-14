from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationintesting.online/")

book_btn = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[9]/div/div/div[3]/button")
book_btn.click()

# Find the draggable element
source_element = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[9]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]')  # Replace 'source-element' with the ID of the element you want to drag

# Find the target element (where you want to drop the draggable element)
target_element = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[9]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[5]')  # Replace 'target-element' with the ID of the target element

# Perform the drag-and-drop operation
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()
