from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class music:
    path = r'C:\Windows\System32\chromedriver.exe'

    def __init__(self):
        
        if self.path:
            # Setup ChromeOptions
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")  # Maximize the browser window
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-infobars")
            
            # Setup ChromeService
            service = Service(executable_path=self.path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        else:
            self.driver = webdriver.Chrome()

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        
        try:
            # Wait until the video title element is visible and clickable
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]')))
            
            # Find the video element and click on it
            video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
            video.click()
        
        except Exception as e:
            print(f"Error: {e}")
            self.driver.quit()

# Usage
#if __name__ == "__main__":
    # Adjust path as necessary
    #assist = music()
    #assist.play("Believer")

    # Ensure proper closing of the browser
    #input("Press Enter to close the browser...")
    #assist.driver.quit()
