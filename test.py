from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver  = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "/html/body/app-root/app-navbar/div/nav/ul/li[2]/a").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = (product.find_element(By.XPATH, "div/h4/a").text)
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li/a').click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div[1]/div[2]/label").click()
driver.find_element(By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div[1]/form/input").click()
print(driver.find_element(By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div[2]/div").text)

time.sleep(6)




# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

