import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import pandas as pd
import getpass
import tkinter as tk
from tkinter import ttk

def scrape_tweets():
    username1 = username_entry.get()
    password1 = password_entry.get()
    n = int(num_tweets_entry.get())
    key = keyword_entry.get()
    name = file_name_entry.get()

    binary = FirefoxBinary('PATH TO BROWSER.EXE')

    # You can change the binary to the browser of your choice

    driver = webdriver.Firefox(executable_path='PATH TO DRIVER', firefox_binary=binary)
    driver.get("https://twitter.com/login")

    sleep(3)
    username = driver.find_element(By.XPATH,"//input[@name='text']")

    username.send_keys(f"{username1}")
    next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
    next_button.click()

    sleep(3)
    password = driver.find_element(By.XPATH,"//input[@name='password']")

    password.send_keys(f'{password1}')
    log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
    log_in.click()

    sleep(3)
    
    driver.get(f"https://twitter.com/search?q={key}&src=typed_query&f=live")

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

    df.to_excel(rf"{name}.xlsx",index=False)
    import os
    os.system(f'start "excel" "{name}.xlsx"')


root = tk.Tk()
root.title("Twitter Scraper")
root.configure(bg="#1F1F1F")

style = ttk.Style()
style.theme_use("clam")

dark_bg = "#1F1F1F"
light_text = "#E0E0E0"
dark_text = "#000000"
accent_color = "#1CA1F2"

style.configure("TLabel", background=dark_bg, foreground=light_text, font=("Segoe UI", 12))
style.configure("TEntry", background=dark_bg, foreground=light_text, fieldbackground=dark_text, font=("Segoe UI", 12))

username_label = ttk.Label(root, text="Twitter Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = ttk.Entry(root, width=30)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = ttk.Label(root, text="Twitter Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

num_tweets_label = ttk.Label(root, text="Number of Tweets:")
num_tweets_label.grid(row=2, column=0, padx=5, pady=5)

num_tweets_entry = ttk.Entry(root, width=30)
num_tweets_entry.grid(row=2, column=1, padx=5, pady=5)

keyword_label = ttk.Label(root, text="Keyword:")
keyword_label.grid(row=3, column=0, padx=5, pady=5)

keyword_entry = ttk.Entry(root, width=30)
keyword_entry.grid(row=3, column=1, padx=5, pady=5)

file_name_label = ttk.Label(root, text="File Name:")
file_name_label.grid(row=4, column=0, padx=5, pady=5)

file_name_entry = ttk.Entry(root, width=30)
file_name_entry.grid(row=4, column=1, padx=5, pady=5)

scrape_button = ttk.Button(root, text="Scrape", command=scrape_tweets, style="Accent.TButton")
scrape_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

def toggle_dark_mode():
    if root["bg"] == dark_bg:
        root["bg"] = "white"
        style.configure("TLabel", background="white", foreground="black")
        style.configure("TEntry", background="white", foreground="black", fieldbackground="white")
        scrape_button.configure(style="TButton")
    else:
        root["bg"] = dark_bg
        style.configure("TLabel", background=dark_bg, foreground=light_text)
        style.configure("TEntry", background=dark_bg, foreground=light_text, fieldbackground=dark_text)
        scrape_button.configure(style="Accent.TButton")

dark_mode_button = ttk.Button(root, text="Dark Mode", command=toggle_dark_mode, style="Accent.TButton")
dark_mode_button.grid(row=0, column=2, padx=5, pady=5)

style.configure("Accent.TButton", background=accent_color, foreground="white", font=("Segoe UI", 10))

root.mainloop()