import random
import smtplib
import time
from email.message import EmailMessage
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

#initialization of webdriver
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
driver.maximize_window()
action=ActionChains(driver)
sign_in_box=driver.find_element_by_xpath("//*[@id='nav-link-accountList']")
action.move_to_element(sign_in_box).perform()
time.sleep(3)
sign_in_btn=driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span")
sign_in_btn.click()
driver.find_element_by_id("ap_email").send_keys("+919902678139")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys("Vandita@1992")
driver.find_element_by_id("signInSubmit").click()

#mobiles
mobiles=driver.find_element_by_xpath("//a[text()='Mobiles']")
mobiles.click()

#searching phone name
driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung A50S")
driver.find_element_by_id("nav-search-submit-button").click()
print(driver.title)
driver.execute_script("window.scrollBy (0,200)","")
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Samsung']").click()
PhoneNames=driver.find_elements_by_css_selector("span[class='a-size-medium a-color-base a-text-normal']")
phonePrice=driver.find_elements_by_xpath("//span[@class='a-price-whole']")

#Excel
myphones=[]
prices=[]
for phone in PhoneNames:
    myphones.append(phone.text)

for price in phonePrice:
    prices.append(price.text)
finalList=zip(myphones,prices)
wb=Workbook()
wb["Sheet"].title="Samsung Data"
sh1=wb.active
sh1.append(["Data","Price"])
for x in list(finalList):
    sh1.append(x)
wb.save("FinalRecords.xlsx")

#Email Sending
msg=EmailMessage()
msg['Subject']="Samsung Phone data"
msg['From']="vandunaik04@gmail.com"
msg['To']="vandunaik04@gmail.com"
msg.set_content("This is for practice purpose")

time.sleep(4)
with open('C:\\Users\\vandi\\PycharmProjects\\Ecommerce_site_automation\\EmailHandling\\EmailTemplate.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

with open("FinalRecords.xlsx","rb") as f:
    file_data=f.read()
    file_name=f.name
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=file_name)


with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:  # same for all
    server.login("vandunaik04@gmail.com","Vandita@1104")
    server.send_message(msg)
print("Email has been sent")


#samsunga50s
time.sleep(3)
driver.execute_script("window.scrollBy(0,600)","")
samsunga50s=driver.find_element_by_css_selector("span[class='a-size-medium a-color-base a-text-normal']")
samsunga50s.click()
time.sleep(5)
driver.execute_script("window.scrollBy(0,200)","")
driver.switch_to_window(driver.window_handles[1])
image_click=driver.find_element_by_css_selector("img[id='landingImage']")
image_click.click()
time.sleep(6)

driver.save_screenshot("C:\\Users\\vandi\\PycharmProjects\\Ecommerce_site_automation\\Screenshot\\image.png")
close_image=driver.find_element_by_xpath("//i[@class='a-icon a-icon-close']")
close_image.click()
time.sleep(4)
add_to_cart=driver.find_element_by_id("add-to-cart-button")
add_to_cart.click()
time.sleep(5)

# driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_id("hlb-ptc-btn-native").click()
time.sleep(3)
driver.find_element_by_css_selector("span[class='a-button-inner']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
