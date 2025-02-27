import calendar

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Initialize WebDriver
driver = webdriver.Chrome()

def navigate_to_url():
    driver.get("https://testautomationpractice.blogspot.com/")
navigate_to_url()
def max_window():
    driver.maximize_window()
max_window()

def gui_elements_handling():
   name =  driver.find_element(By.XPATH ,'//*[@id="name"]')
   name.send_keys('shyam')

   email = driver.find_element(By.XPATH , '//*[@id="email"]')
   email.send_keys('prayagsoni651@gmail.com')

   phone_no = driver.find_element(By.XPATH , '//*[@id="phone"]')
   phone_no.send_keys('7828255673')

   address = driver.find_element(By.XPATH   , '//*[@id="textarea"]')
   address.send_keys('Bhopal')

gui_elements_handling()
time.sleep(10)
print('test  case passed ')

def select_options():
    male_female = driver.find_element(By.XPATH ,'//*[@id="male"]')
    male_female.click()

    days = driver.find_element(By.XPATH , '//*[@id="sunday"]')
    days.click()
select_options()


def select_dropdown_element():
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "country"))  # Replace with the correct locator
    )

    # Create a Select object
    select = Select(dropdown)

    # Select an option by visible text
    select.select_by_index(9)
select_dropdown_element()


def select_color():
    color = driver.find_element(By.XPATH , '//*[@id="colors"]/option[4]')
    color.click()
select_color()


def select_sorted_list():
    select_lion = driver.find_element(By.XPATH , '//*[@id="animals"]/option[8]')
    select_lion.click()
select_sorted_list()


def select_date_picker_1():
    y = '2002'  # Target year
    m = 'December'  # Target month (full name as displayed on the date picker)
    d = '15'  # Target date

    try:

        # Open the date picker by clicking on the input field
        date_input = driver.find_element(By.ID, "datepicker")
        date_input.click()

        # Wait for the date picker to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-calendar"))
        )

        while True:
            # Capture the current month and year
            month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
            year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

            # Compare with the target month and year
            if month == m and year == y:
                break
            else:
                # Determine whether to click "Next" or "Previous"
                current_year = int(year)
                target_year = int(y)
                current_month = list(calendar.month_name).index(month)
                target_month = list(calendar.month_name).index(m)

                if (current_year < target_year) or (current_year == target_year and current_month < target_month):
                    # Click the "Next" button to navigate to the next month
                    next_button = driver.find_element(By.XPATH, "//a[@title='Next']")
                    next_button.click()
                else:
                    # Click the "Previous" button to navigate to the previous month
                    prev_button = driver.find_element(By.XPATH, "//a[@title='Prev']")
                    prev_button.click()

        # Capture all the date elements
        all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td/a")

        # Select the target date
        for date_element in all_dates:
            if date_element.text == d:
                date_element.click()
                break

        print("Date selected successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Switch back to the main content (if you switched to an iframe)
        driver.switch_to.default_content()
select_date_picker_1()

def select_date_picker_1():
    y = '2002'  # Target year
    m = 'December'  # Target month (full name as displayed on the date picker)
    d = '15'  # Target date

    try:

        # Open the date picker by clicking on the input field
        date_input = driver.find_element(By.ID, "datepicker")
        date_input.click()

        # Wait for the date picker to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-calendar"))
        )

        while True:
            # Capture the current month and year
            month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
            year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

            # Compare with the target month and year
            if month == m and year == y:
                break
            else:
                # Determine whether to click "Next" or "Previous"
                current_year = int(year)
                target_year = int(y)
                current_month = list(calendar.month_name).index(month)
                target_month = list(calendar.month_name).index(m)

                if (current_year < target_year) or (current_year == target_year and current_month < target_month):
                    # Click the "Next" button to navigate to the next month
                    next_button = driver.find_element(By.XPATH, "//a[@title='Next']")
                    next_button.click()
                else:
                    # Click the "Previous" button to navigate to the previous month
                    prev_button = driver.find_element(By.XPATH, "//a[@title='Prev']")
                    prev_button.click()

        # Capture all the date elements
        all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td/a")

        # Select the target date
        for date_element in all_dates:
            if date_element.text == d:
                date_element.click()
                break

        print("Date selected successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Switch back to the main content (if you switched to an iframe)
        driver.switch_to.default_content()
select_date_picker_1()



def select_year_from_dropdown_picker_2():
    try:
        # Open the datepicker by clicking on the input field
        date_picker = driver.find_element(By.XPATH, '//*[@id="txtDate"]')
        date_picker.click()

        # Wait for the year dropdown to be present
        month_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[1]'))
        )

        # Create a Select object for the year dropdown
        month_select = Select(month_dropdown)

        # Select the year by visible text
        month_select.select_by_visible_text("Dec")  # Replace with the desired year

        print("month selected successfully!")

    except Exception as e:
        print(f"Error: {e}")




    try:
        # Open the datepicker by clicking on the input field
        date_picker = driver.find_element(By.XPATH, '//*[@id="txtDate"]')
        date_picker.click()

        # Wait for the year dropdown to be present
        year_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[2]'))
        )

        # Create a Select object for the year dropdown
        year_select = Select(year_dropdown)

        # Select the year by visible text
        year_select.select_by_visible_text("2015")  # Replace with the desired year

        print("Year selected successfully!")

    except Exception as e:
        print(f"Error: {e}")


    try:
        date = driver.find_element(By.XPATH , '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[3]/a')
        date.click()
    except Exception as e:
        print('date was not selected')

select_year_from_dropdown_picker_2()



def date_picker_select_date_range():

    date_ = driver.find_element(By.XPATH , '//*[@id="start-date"]')
    date_.send_keys('15-12-2002')

    date__ = driver.find_element(By.XPATH , '//*[@id="end-date"]')
    date__.send_keys('1-02-2025')

    submit_button = driver.find_element(By.XPATH , '//*[@id="post-body-1307673142697428135"]/div[8]/button')
    submit_button.click()

date_picker_select_date_range()


def upload_single_file():
    try:
        # Locate the file input element
        file_input = driver.find_element(By.XPATH, '//*[@id="singleFileInput"]')

        # Provide the path to the file you want to upload
        file_path = r'C:\Users\praya\OneDrive\Desktop\Writing effective automation test c.txt'
        file_input.send_keys(file_path)
        upload = driver.find_element(By.XPATH , '//*[@id="singleFileForm"]/button')
        upload.submit()

        print("File uploaded successfully!")

    except Exception as e:
        print(f"Error: {e}")
upload_single_file()


def upload_multiple_files():
    try:
        # Locate the file input element
        file_input = driver.find_element(By.XPATH, '//*[@id="multipleFilesInput"]')

        # Provide the paths to the files you want to upload (separated by \n)
        file_paths = "\n".join([
            r'C:\Users\praya\OneDrive\Desktop\QA (Quality Assurance) Syllabus.txt',
            r'C:\Users\praya\OneDrive\Desktop\FSDA 23rd SQL queries  (1) (2).txt',
            r'C:\Users\praya\OneDrive\Desktop\fsda mysql installation.txt',
            r'C:\Users\praya\OneDrive\Desktop\FSDA 23rd SQL queries  (1).txt',
            r'C:\Users\praya\OneDrive\Desktop\LSTM or GRU.txt'
        ])

        # Send the file paths to the file input element
        file_input.send_keys(file_paths)

        # Locate and click the upload button
        upload_button = driver.find_element(By.XPATH, '//*[@id="multipleFilesForm"]/button')
        upload_button.click()

        print("Files uploaded successfully!")

    except Exception as e:
        print(f"Error: {e}")


# Assuming you have already initialized the `driver` object
# driver = webdriver.Chrome()  # or any other driver
upload_multiple_files()


def handling_dynamic_button():
    try:
        # Wait for the button to be clickable
        dynamic_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="HTML5"]/div[1]/button'))
        )
        dynamic_button.click()
        print("Dynamic button clicked successfully!")

    except Exception as e:
        print(f"Error clicking dynamic button: {e}")
handling_dynamic_button()


def handling_simple_alert_window():
    try:
        # Click the button that triggers the alert
        alert_button = driver.find_element(By.XPATH, "//button[@id='alertBtn']")
        alert_button.click()
        print("Alert triggered.")

        # Switch to the alert
        alert = driver.switch_to.alert
        print(f"Alert text: {alert.text}")  # Optional: Print the alert text

        # Accept the alert
        alert.accept()
        print("Alert accepted.")

    except Exception as e:
        print(f"Error handling alert: {e}")

handling_simple_alert_window()


def confirmation_alert():
    try:
        # Click the button that triggers the confirmation alert
        confirm_button = driver.find_element(By.XPATH, "//button[@id='confirmBtn']")
        confirm_button.click()
        print("Confirmation alert triggered.")

        # Switch to the alert
        alert = driver.switch_to.alert
        print(f"Confirmation alert text: {alert.text}")  # Optional: Print the alert text

        # Accept the alert (click "OK")
        alert.accept()
        print("Confirmation alert accepted.")

        # Alternatively, dismiss the alert
        # alert.dismiss()
        # print("Confirmation alert dismissed.")

    except Exception as e:
        print(f"Error handling confirmation alert: {e}")
confirmation_alert()


def prompt_alert():
    try:
        prompt_button = driver.find_element(By.XPATH , "//button[@id='promptBtn']")
        prompt_button.click()

        popup = driver.switch_to.alert
        popup.accept()
        print('prompt alert accepted')
    except Exception as e:
        print(f'Error in accepting the prompt_button: {e}')
prompt_alert()


def handle_new_window():
    try:
        # Get the handle of the original tab
        original_tab = driver.current_window_handle
        print(f"Original tab handle: {original_tab}")

        # Perform the action that opens a new tab (e.g., clicking a link)
        new_tab_link = driver.find_element(By.XPATH, "//button[@onclick='myFunction()']")  # Replace with the correct locator
        new_tab_link.click()
        print("New tab opened.")

        # Wait for the new tab to open
        time.sleep(5)  # Adjust the sleep time as needed

        # Get all window handles
        all_tabs = driver.window_handles
        print(f"All tab handles: {all_tabs}")

        # Switch to the new tab
        new_tab = [tab for tab in all_tabs if tab != original_tab][0]
        driver.switch_to.window(new_tab)
        print("Switched to the new tab.")

        # Perform actions in the new tab
        print(f"New tab URL: {driver.current_url}")
        # add a code to perform a many operations
        time.sleep(5)

        # Close the new tab (optional)
        driver.close()
        print("New tab closed.")

        # Switch back to the original tab
        driver.switch_to.window(original_tab)
        print("Switched back to the original tab.")

    except Exception as e:
        print(f"Error handling new tab: {e}")
handle_new_window()


def handling_popup_tab():
    try:
        # Get the handle of the original window
        original_window = driver.current_window_handle

        # Click the button that opens a new window or tab
        popup_button = driver.find_element(By.XPATH, "//button[@id='PopUp']")
        popup_button.click()

        # Wait for the new window or tab to open
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

        # Switch to the new window or tab
        for handle in driver.window_handles:
            if handle != original_window:
                driver.switch_to.window(handle)
                break

        print(f"New window/tab URL: {driver.current_url}")

        # Perform actions in the new window or tab
        # ...

        # Close the new window or tab
        driver.close()

        # Switch back to the original window
        driver.switch_to.window(original_window)
        print("Switched back to the original window.")

    except Exception as e:
        print(f"Error handling browser popup: {e}")
handling_popup_tab()


def handling_mouse_hover():
    try:
        point_me =driver.find_element(By.XPATH , "//button[@class='dropbtn']")
        mobiles = driver.find_element(By.XPATH , "//a[normalize-space()='Mobiles']")
        laptops = driver.find_element(By.XPATH , "//a[normalize-space()='Laptops']")

        act = ActionChains(driver)
        act.move_to_element(point_me).move_to_element(mobiles).move_to_element(laptops).click().perform()
        print('laptops actions performed successful')


    except Exception as e:
        print(f"Error handling mouse hover: {e}")
handling_mouse_hover()


driver.close()

time.sleep(5)




