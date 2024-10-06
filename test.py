from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://pk.indeed.com/cmp/Cloudlogically")
jobs = driver.find_element(By.CSS_SELECTOR,"#cmp-skip-header-desktop .eu4oa1w0:nth-child(5) .eu4oa1w0")
print(jobs.text)
