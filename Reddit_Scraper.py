import tkinter as tk
from tkinter import ttk

def scrape_reddit():
    import pandas as pd
    import praw


    username = username_entry.get()
    password = password_entry.get()
    subreddit_name = subreddit_entry.get()
    file_name = file_name_entry.get()
    number = int(num_entry.get())

    # Get your client ID and secret from https://www.reddit.com/prefs/apps
    
    reddit = praw.Reddit(
        client_id="your_id",
        client_secret="your_secret",
        username=username,
        password=password,
        user_agent="your_user_agent",
    )

    subreddit = reddit.subreddit(subreddit_name)

    titles = []
    scores = []
    comments = []

    for post in subreddit.hot(limit=number):

        titles.append(post.title)
        scores.append(post.score)
        post_author = post.author.name

        post.comments.replace_more(limit=None)
        post_comments = []
        for comment in post.comments.list():
            comment_text = f"{comment.author.name}: {comment.body}"
            post_comments.append(comment_text)

        comments.append("\n".join(post_comments))

    data = {
        "Title": titles,
        "Score": scores,
        "Post_author": post_author,
        "Comments": comments,
    }
    df = pd.DataFrame(data)

    df.to_csv(f'{file_name}.csv', index=False)

root = tk.Tk()
root.title("Reddit Scraper")
root.configure(bg="#1F1F1F")

style = ttk.Style()
style.theme_use("clam")

dark_bg = "#1F1F1F"
light_text = "#E0E0E0"
dark_text = "#000000"
accent_color = "#FF4500"

style.configure("TLabel", background=dark_bg, foreground=light_text, font=("Segoe UI", 12))
style.configure("TEntry", background=dark_bg, foreground=light_text, fieldbackground=dark_text, font=("Segoe UI", 12))

username_label = ttk.Label(root, text="Reddit Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = ttk.Entry(root, width=30)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = ttk.Label(root, text="Reddit Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

subreddit_label = ttk.Label(root, text="Subreddit Name:")
subreddit_label.grid(row=2, column=0, padx=5, pady=5)

subreddit_entry = ttk.Entry(root, width=30)
subreddit_entry.grid(row=2, column=1, padx=5, pady=5)

file_name_label = ttk.Label(root, text="File Name:")
file_name_label.grid(row=3, column=0, padx=5, pady=5)

file_name_entry = ttk.Entry(root, width=30)
file_name_entry.grid(row=3, column=1, padx=5, pady=5)

num_label = ttk.Label(root, text="Number of Posts:")
num_label.grid(row=4, column=0, padx=5, pady=5)

num_entry = ttk.Entry(root, width=30)
num_entry.grid(row=4, column=1, padx=5, pady=5)

scrape_button = ttk.Button(root, text="Scrape", command=scrape_reddit, style="Accent.TButton")
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