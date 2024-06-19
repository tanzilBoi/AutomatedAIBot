from selenium import webdriver
from selenium.webdriver.common.by import By

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def executable_path_set(self, path):
        path="C:\\Windows\\System32\chromedriver.exe"
        self.driver.close()  # Close the existing driver session
        self.driver = webdriver.Chrome(executable_path=path)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        
        search_input = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search_input.send_keys(query)
        
        search_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        search_button.click()

# Example usage

#assist = infow()
#assist.get_info("neutron stars")  # Provide a query string here

#input("Press Enter to close the browser...")  # Wait for user input to close
#assist.driver.quit()  # Close the browser after manual confirmation
