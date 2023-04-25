import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import pandas as pd

PATH = "C:/Users/amrit/Downloadsgeckodriver.exe"

n = int(input("Enter the number of tweets you want to scrape: "))
key = input("Enter the keyword you want to search for: ")

binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
driver = webdriver.Firefox(executable_path='C:/Users/amrit/Downloads/geckodriver.exe', firefox_binary=binary)
driver.get("https://twitter.com/login")

sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")

username.send_keys("parikshan160951")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")

password.send_keys('drowsycodevit')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")

search_box.send_keys(key)
search_box.send_keys(Keys.ENTER)

sleep(3)
latest = driver.find_element(By.XPATH,f"//a[@href='/search?q={key}&src=typed_query&f=live']")
latest.click()

UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")

while len(Tweets) < n:
    for article in articles:
        try:
            for i in range(1, n):
                tweet_handle = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[{i}]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/a/div/span').text
                UserTags.append(tweet_handle)
        except:
            UserTags.append('')

        try:

            TimeStamp = article.find_element(By.XPATH,".//time").get_attribute('datetime')
            TimeStamps.append(TimeStamp)

        except:
            TimeStamps.append('')

        try:
            Tweet = article.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
            Tweets.append(Tweet)
        except:
            Tweets.append('')

        try:
            for i in range(1, n):
                Reply = article.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[{i}]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[1]/div/div/div[2]/span/span/span").text
                Replys.append(Reply)
        except:
            Replys.append('')

        try:
            for i in range(1, n):
                reTweet = article.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[{i}]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/div[2]/span/span/span").text
                reTweets.append(reTweet)
        except:
            reTweets.append('')

        try:
            for i in range(1,n):
                Like = article.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[{i}]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[3]/div/div/div[2]/span/span/span").text
                Likes.append(Like)
        except:
            Likes.append('')

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

    sleep(3)
    if len(Tweets) >= n:
        break
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets = list(set(Tweets))

df = pd.DataFrame(zip(UserTags,TimeStamps,Tweets,Replys,reTweets,Likes)
,columns=['UserTags','TimeStamps','Tweets','Replys','reTweets','Likes'])

df.to_excel(r"tweets.xlsx",index=False)
import os
os.system('start "excel" "tweets.xlsx"')