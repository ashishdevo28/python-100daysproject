from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options 

usr=input('Enter Email Id:')
pwd=input('Enter Password:')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print('Opened FB')
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email if entered")
sleep(1)

unername_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print('Password Entered')

login_box = driver.find_element_by_id('loginbutton')
login_blox.click()

print("DONE")
input('Print any key to quit')
driver.quit()
print('Finished')