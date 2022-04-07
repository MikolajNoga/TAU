from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

# Provide the path of chromedriver present on your system.
driver = webdriver.Chrome(executable_path="C:\\Users\\nogam\\Desktop\\chromedriver.exe", chrome_options=options)

logger.info('Opening fuel cost calculator site')
driver.get('https://www.calculator.net/fuel-cost-calculator.html')

logger.info('Setting inputs to form')

driver.find_element(by=By.CLASS_NAME, value="clearbtn").click()

driver.find_element(by=By.NAME, value="tripdistance").send_keys("1000")
driver.find_element(by=By.XPATH, value='//select[@name="tripdistanceunit"]/option[text()="miles"]').click()

driver.find_element(by=By.NAME, value="fuelefficiency").send_keys("6")
driver.find_element(by=By.XPATH, value='//select[@name="fuelefficiencyunit"]/option[text()="liters per 100 km (L/100 '
                                       'km)"]').click()

driver.find_element(by=By.NAME, value="gasprice").send_keys("2.5")
driver.find_element(by=By.XPATH, value='//select[@name="gaspriceunit"]/option[text()="per liter"]').click()

driver.find_element(by=By.XPATH, value='//input[@value="Calculate"]').click()

if driver.find_element(by=By.XPATH, value='//b[text()="96.6"]')\
        and driver.find_element(by=By.XPATH, value='//b[text()="$241.4"]'):
    logger.info('Correct values')
else:
    logger.warning('Wrong values')

driver.close()
