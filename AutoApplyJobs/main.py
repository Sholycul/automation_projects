from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

path = r"C:\Users\FIDO\PycharmProjects\chromedriver-win32\chromedriver.exe"

driver = webdriver.Chrome(service=ChromeService(executable_path=path))

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3847935128&f_LF=f_AL&geoId=102748797&keywords=python%20developer&location=Texas%2C%20United%20States&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true")

time.sleep(20)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(30)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys("ijioluwasholamichael@gmail.com")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("pFr8M#cSzXd+-4i")
driver.find_element(By.CLASS_NAME, "login__form_action_container ").click()

time.sleep(15)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
# all_listings = driver.find_elements(By.CSS_SELECTOR, ".ember-view")
all_jobs = [job.get_property("a") for job in all_listings]
print(all_jobs)

for listing in all_listings:
    print(listing.get_property("a"))
    # driver.execute_script("arguments[0].click();", listing)
    listing.click()
    time.sleep(12)


    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.XPATH, "//div[@class='display-flex']/child::div[@class='jobs-s-apply "
                                                        "jobs-s-apply--fadein inline-flex mr2']")
        # driver.execute_script("arguments[0].click();", apply_button)
        apply_button.click()
        time.sleep(15)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("09059538784")

        submit_button = driver.find_element(By.LINK_TEXT, "Submit application")
        time.sleep(50)
        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element(By.XPATH, '//button[@aria-label="Dismiss"]').click()
            time.sleep(12)
            discard_button = driver.find_element(By.XPATH, '//button[@data-control-name="discard_application_confirm_btn"]').click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(20)
        close_button = driver.find_element(By.XPATH, '//button[@aria-label="Dismiss"]').click()


    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)




























































# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://www.linkedin.com/home")
# content = response.text
# # print(content)

# soup = BeautifulSoup(content, "html.parser")
# btn = soup.find_all("button")

# print(btn)