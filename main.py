from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



link = "https://kahoot.it/"
name = input("Name: ")
pin = str(input("PIN: "))
bots = int(input("Bots: "))



driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

for i in range(bots):
    driver.execute_script('''window.open("https://kahoot.it/","_blank");''')
    driver.switch_to.window(driver.window_handles[i+2])
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/main/div/form/input")))
    inputid = driver.find_element(By.ID, 'game-input')
    inputid.send_keys(pin)
    inputid.send_keys(Keys.ENTER)
    wait.until(EC.visibility_of_element_located((By.ID, 'nickname')))
    inputname = driver.find_element(By.ID, 'nickname')
    namein = str(f"{name}_{i}")
    print("Logging in: ", namein)
    inputname.send_keys(namein)
    inputname.send_keys(Keys.ENTER)

while True:
    pass