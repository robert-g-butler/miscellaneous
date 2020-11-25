
import pathlib as Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
time.sleep(5)

# Update "Time and Sales Historical Data", "Type of Data" to "Trade Cancellation"
type_of_data_dropdown = driver.find_element_by_xpath('//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[1]/label/span[2]/input')
type_of_data_dropdown.click()
time.sleep(5)

trade_cancellation_option = driver.find_element_by_xpath('//*[@id="sgx-select-dialog"]/div[2]/sgx-select-picker/sgx-list/div/div/sgx-select-picker-option[3]')
trade_cancellation_option.click()
time.sleep(5)

# Download "Time and Sales Historical Data"
download_button = driver.find_element_by_xpath('//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/button')
download_button.click()
time.sleep(5)

# Close the Chrome browser
driver.close()
