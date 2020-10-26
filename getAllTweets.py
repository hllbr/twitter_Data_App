from selenium import webdriver
import loginInfo
from selenium.webdriver.common.keys import Keys
import time

browser =webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div[2]/a[2]/div/span/span")

giris_yap.click()

time.sleep(3)

username = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")

password = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")


username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)

login = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
login.click()

time.sleep(3)

aratalım = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")



aratalım.send_keys("#yazilimayolver")
aratalım.send_keys(Keys.ENTER)

time.sleep(3)
tweetler = set()
tweetField = browser.find_elements_by_css_selector(".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim")
for tweet in tweetField:
    tweetler.add(tweet.text)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
tweetCount = 1
with open("tweets.txt","w", encoding= "UTF-8") as file:
    for tweet in tweetler\
            :
        file.write(str(tweetCount) +"\n"+ tweet +"\n")
        file.write("**************************************************\n")
        tweetCount+=1
time.sleep(1)



browser.close()
