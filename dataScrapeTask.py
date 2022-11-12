from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://perfumancebd.com/product-category/perfume/refreshing/")
print('Task 01 Output From Here______________________________________')
#Task 01 Print Section
for i in range(1, 12):
 driver.get("https://perfumancebd.com/product-category/perfume/refreshing/")
 title = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/p[1]')
 price = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/p[2]')
 image = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/a/img')

 print('Product Title', title.text)
 print('Product Price', price.get_attribute('innerHTML'))
 print('Product Image', image.get_attribute('src'))

#Task 01 Photo Section
for i in range(1, 12):
 driver.get("https://perfumancebd.com/product-category/perfume/refreshing/")
 image = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/a/img')
 dwn = image.get_attribute('src')
 driver.get(dwn)
 img_loc = "G:/EuropeanITSoulution/Class 12/Task 01 Photos/attar"+str(i)+".png"
 driver.save_screenshot(img_loc)

print('Task 02 Output From Here ______________________________________')
# Task 02 Print Section
for i in range(1, 12):
 driver.get("https://perfumancebd.com/product-category/perfume/calm-and-cool/")
 title = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/p[1]')
 price = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/p[2]')
 image = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/a/img')

 print('Product Title', title.text)
 print('Product Price', price.get_attribute('innerHTML'))
 print('Product Image', image.get_attribute('src'))

#Task 02 Photo Section
for i in range(1, 12):
 driver.get("https://perfumancebd.com/product-category/perfume/calm-and-cool/")
 image = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div[' + str(i) + ']/a/img')
 dwn = image.get_attribute('src')
 driver.get(dwn)
 img_loc = "G:/EuropeanITSoulution/Class 12/Task 02 Photos/attar" + str(i) + ".png"
 driver.save_screenshot(img_loc)

driver.quit()
