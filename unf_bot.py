from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import getpass
import ast
sleep(1)
# username = input("Username: ")
# pw = getpass.getpass("Password: ")
username = 'tardssz'
pw = 'babyshark3'

not_following = ast.literal_eval(open("/Users/mac/Desktop/Tests/PyTests/files/output.txt", "r").read())

class InstaBot:
    def __init__(self, username, pw):
        self.service = Service(executable_path='/Users/mac/Documents/Python/chromedriver')
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)

        self.driver.find_element("xpath","//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element("xpath","//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element("xpath",'//button[@type="submit"]')\
            .click()
        sleep(10)

    def unfollow(self, nf_file):
        i = 0
        while i != len(not_following):
            self.target = nf_file[i]

            self.driver.get("https://www.instagram.com/"+self.target)
            sleep(5)
            if self.driver.current_url == "https://www.instagram.com/"+self.target:
                try:
                    try:
                        num_followers = self.driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").text
                        num_following = self.driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a").text
                        print(i,len(not_following),end="\r")
                        print(self.target,num_followers,num_following,end="\r")
                    except:
                        continue
                    
                    self.driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button")\
                        .click()
                    sleep(2)

                    self.driver.find_element("xpath","/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div/div/div")\
                        .click()
                    sleep(2)
                    
                except:
                    continue
                
                finally:
                    i += 1

InstaBot(username,pw).unfollow(not_following)