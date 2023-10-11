    
from selenium import webdriver
import time


#initialising class
class Tester:
    def __init__(self,is_web=True,browser_type=None,headless=False):
        # for testing web applications
        if is_web:
            if browser_type == "chrome":                
                chrome_options = webdriver.ChromeOptions()
                if headless == "True":
                    chrome_options.add_argument('--headless')
                else:
                    chrome_options.add_argument('--head')
                self.driver = webdriver.Chrome(options=chrome_options)

            elif browser_type == "firefox":
                chrome_options = webdriver.FirefoxOptions()
                if headless == "True":
                    chrome_options.add_argument('--headless')
                else:
                    chrome_options.add_argument('--head')
                self.driver = webdriver.Firefox(options=chrome_options)

            elif browser_type == "safari":
                chrome_options = webdriver.SafariOptions()
                if headless == "True":
                    chrome_options.add_argument('--headless')
                else:
                    chrome_options.add_argument('--head')
                self.driver = webdriver.Safari(options=chrome_options)

            elif browser_type == "microsoft edge":
                chrome_options = webdriver.EdgeOptions()
                if headless == "True":
                    chrome_options.add_argument('--headless')
                else:
                    chrome_options.add_argument('--head')
                self.driver = webdriver.Edge(options=chrome_options)
            else:
                raise ValueError("Unsupported browser type")
        # for testing Mobile applications
        else:
            pass 
    # redirecting to given URL
    def get(self,url):
        self.driver.get(url)
        time.sleep(3)
        print("Execution completed successfully")
    # closing automation process
    def close(self):
        self.driver.quit()

def main():
    automation_type = input("Select Automation Type (web/mobile):").lower()
    
    if(automation_type == "web"):
        browser_type = input("Select Browser Type (chrome/firefox/safari/microsoft edge):").lower()
        head_type = input("Run in headless mode? (True/False):")
        url = input("Enter URL to Automation: ")
        try:
            automation = Tester(is_web=True,browser_type=browser_type,headless=head_type)
            automation.get(url)
            automation.close()
        except ValueError as e:
            print(e)
            return
      
    elif(automation_type == "mobile"):
      print("Mobile automation is enabled")
      """   try:
            automation = Tester(is_web=False,browser_type=browser_type,headless=head_type)
            automation.get(url)
            automation.close()
        except ValueError as e:
            print(e)
            return  """
      
    else:
        print("Please enter valid automation type")

if __name__=="__main__":
    main()