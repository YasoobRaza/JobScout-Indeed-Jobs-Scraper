from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import string

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# not using headless mode (can't by pass cloudfare bot detection) 
driver = webdriver.Chrome()
driver.minimize_window()

## for complete run
# l = None 
# p = None
# c = None

# controlled test
l = 3 # to select range of letters
p = 3 # to select range of pages for each letter
c = 3# to select no of companies from a each page of a letter


letters = string.ascii_uppercase

# iterating over letter pages
for letter in letters[:l]:
    df = pd.DataFrame(columns=['Company', 'number of jobs','page num'])
    driver.get(f"https://www.indeed.com/companies/browse-companies/{letter}")
    print(driver.get)
    # getting all pages for a letter
    pages = driver.find_elements(By.CSS_SELECTOR, ".css-u74ql7 .e1wnkr790")
    page_list = [page.text for page in pages]

    # iterating over all pages of a letter
    for page in page_list[:p]:
        driver.find_element(By.LINK_TEXT,page).click()
        # getting all companies on a page
        companies = driver.find_elements(By.CSS_SELECTOR, ".css-1bx5raa:nth-child(1) .e1wnkr790")
        company_list = [company.text for company in companies]
        
        # iterating over all companies on a page
        for company in company_list[:c]:
            driver.find_element(By.LINK_TEXT,company).click()
            try:
                jobs = driver.find_element(By.CSS_SELECTOR,"#cmp-skip-header-desktop .eu4oa1w0:nth-child(5) .eu4oa1w0").text
            except:
                jobs = 0

            row = (company,jobs,page)
            print(row)  #test  
            df.loc[len(df)] = row

            driver.back()
    # separate csv for each letter
    df.to_csv(f'data/companies with {letter}.csv',index=False)     
