import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

path = r"C:\Users\FIDO\PycharmProjects\chromedriver-win32\chromedriver.exe"
driver = webdriver.Chrome(service=ChromeService(executable_path=path))

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3861919501&geoId=105365761&keywords=Python%20developer&location=Nigeria&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true"

driver.get("https://www.linkedin.com/login")
# driver.get(URL)
# time.sleep(10)
# sign_in_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
# sign_in_button.click()

try:
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys("ijioluwasholamichael@gmail.com")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("pFr8M#cSzXd+-4i")

    password_field.send_keys(Keys.ENTER)

    time.sleep(20)
    jobs = driver.find_element(By.LINK_TEXT, "Jobs")
    jobs.click()

    time.sleep(20)
    job_title = driver.find_element(By.CLASS_NAME, "jobs-search-box__search-icon--custom")
    job_title.click()
    job_title.send_keys("Python developer")

    # location = driver.find_element(By.ID, "jobs-search-box-location-id-ember393")
    # location.send_keys("Nigeria")

    job_title.send_keys(Keys.ENTER)

    easy_apply = driver.find_element(By.PARTIAL_LINK_TEXT, "Easy Apply")
    easy_apply.click()
except NoSuchElementException:
    time.sleep(30)



driver.quit()
