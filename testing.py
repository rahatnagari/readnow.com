import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




driver = webdriver.Chrome()
#home to books button
driver.get("http://127.0.0.1:8000/home/")

time.sleep(4)
books_button = driver.find_element(By.XPATH, "/html/body/ul/li[4]/a")
time.sleep(2)
books_button.click()
time.sleep(4)

if "this is book browsing page" in driver.page_source:
    print("Logged in to book page- segment success")
else:
    print("not logged in")

#home to login button
driver.get("http://127.0.0.1:8000/home/")

time.sleep(4)
login_button = driver.find_element(By.XPATH, "/html/body/ul/li[2]/a")
login_button.click()

if "Click the submit button to login" in driver.page_source:
    print("Logged in to log-in page- segment success")
else:
    print("not logged in")

time.sleep(4)
userid = driver.find_element(By.XPATH, "/html/body/div[2]/center/form/input[1]")
userid.send_keys("18201003")
time.sleep(2)
password = driver.find_element(By.XPATH, "/html/body/div[2]/center/form/input[2]")
password.send_keys("1234 ")


time.sleep(4)
login_button = driver.find_element(By.XPATH, "/html/body/div[2]/center/form/a/button")
login_button.click()

if "This is User Profile Page" in driver.page_source:
    print("Logged in to User profile page- segment success")
else:
    print("not logged in")

#home to regirtry page

time.sleep(4)
home_button = driver.find_element(By.XPATH, "/html/body/ul/li[1]/a")
home_button.click()
time.sleep(2)
becomeamember_button = driver.find_element(By.XPATH, "/html/body/ul/li[3]/a")
becomeamember_button.click()
time.sleep(2)
if "Become a member to explore free books" in driver.page_source:
    print("Logged in to Registy page- segment success")
else:
    print("not logged in")
#member form fillig
time.sleep(2)
fastname = driver.find_element(By.XPATH, "/html/body/div[2]/center/form/input[1]")
fastname.send_keys("Obaidul")
time.sleep(1)
lastname = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[2]")
lastname.send_keys("Kader")
time.sleep(1)
day = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[3]")
day.send_keys("09")
time.sleep(1)
month = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[4]")
month.send_keys("March")
time.sleep(1)
year = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[5]")
year.send_keys("1996")
time.sleep(1)
mobile_number = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[6]")
mobile_number.send_keys("01971429831")
time.sleep(1)
country = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[7]")
country.send_keys("Bangladesh")
time.sleep(1)
district = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[8]")
district.send_keys("Dhaka")
time.sleep(1)
profession = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[9]")
profession.send_keys("Engineer")
time.sleep(1)
setpassword = driver.find_element(By.XPATH,"/html/body/div[2]/center/form/input[10]")
setpassword.send_keys("1234")
time.sleep(3)
create_profile = driver.find_element(By.XPATH, "/html/body/div[2]/center/form/a/button")
create_profile.click()
if "This is User Profile Page" in driver.page_source:
    print("Logged in to User Profile page- segment success")
else:
    print("not logged in")








