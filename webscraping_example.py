
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

DRIVER_FILEPATH = r'C:\Users\robbi\Downloads\webscraping_example\chromedriver_v87.exe'
NEW_DOWNLOADS_FOLDERPATH = r'C:\Users\robbi\Downloads\webscraping_example'

# Set options for opening a Chrome browser / driver
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--window-size=900,900')
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': NEW_DOWNLOADS_FOLDERPATH,
    'directory_upgrade': True,
    'download.prompt_for_download': False,
    'safebrowsing.enabled': True,})

# Open the Chrome browser
driver = webdriver.Chrome(executable_path=DRIVER_FILEPATH,
                          options=chrome_options)

# Go to the website
driver.get('https://www.sgx.com/research-education/derivatives')

# Specify the xpaths of the "Time and Sales Historical Data" dropdowns and download button
TYPE_DROPDOWN_XPATH = '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[1]/label/span[2]/input'
TYPE_OPTION_XPATH = '//*[@id="sgx-select-dialog"]/div[2]/sgx-select-picker/sgx-list/div/div/sgx-select-picker-option[3]'

DATE_DROPDOWN_XPATH = '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[2]/label/span[2]/input'
DATE_OPTION_XPATH = '//*[@id="sgx-select-dialog"]/div[2]/sgx-select-picker/sgx-list/div/div/sgx-select-picker-option[1]'

DOWNLOAD_BUTTON_XPATH = '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/button'



# Open the "Type of Data" dropdown menu by clicking on it
type_dropdown = WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, TYPE_DROPDOWN_XPATH)))
time.sleep(1)
type_dropdown.click()

# Click the "Trade Cancellation" option
type_option = WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, TYPE_OPTION_XPATH)))
time.sleep(1)
type_option.click()



# Open the "Date" dropdown menu by clicking on it
date_dropdown = WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, DATE_DROPDOWN_XPATH)))
time.sleep(1)
date_dropdown.click()

# Click the "Trade Cancellation" option
date_option = WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, DATE_OPTION_XPATH)))
time.sleep(1)
date_option.click()



# Click the download button
download_button = WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, DOWNLOAD_BUTTON_XPATH)))
time.sleep(1)
download_button.click()
time.sleep(5)



# Close the Chrome browser
driver.close()

