# Social Media Scraper

<img src="https://website.understandingdata.com/wp-content/uploads/2022/02/scraping-twitter-1024x440.jpg" alt="Scraping Twitter" width="512" height="220" />

## Introduction
This program is a Python script that utilizes the Selenium web driver and the PRAW (Python Reddit API Wrapper) library to scrape a specified number of tweets containing a particular keyword from Twitter and a specified number of posts from a subreddit on Reddit. The scraped data is stored in an Excel file that can be easily accessed and analyzed.

<img src="https://i.imgur.com/JS9bxEB.png" alt="Scraping Twitter"/>
<hr>
<img src="https://imgur.com/DlfeMQ5.png" alt="Scraping Reddit"/>

## Dependencies
To use this program, you need to have the following installed on your system:
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
- `Python Reddit API Wrapper | PRAW`

You can install these dependencies using pip, by running the following commands:
```
pip install selenium
pip install pandas
pip install praw
```
## How to Use
### ![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)
1. Clone this repository or download the script to your local machine.
2. Open the script in a Python IDE or text editor.
3. Change the path of your Firefox binary and geckodriver executable on lines 17 and 18.
4. Run the script and enter the required inputs in the command prompt when prompted:
    - Your Twitter username
    - Your Twitter password
    - The number of tweets you want to scrape
    - The keyword you want to search for
    - The name of the Excel file to be stored
5. The script will start scraping tweets and store them in an Excel file with the specified name.
6. The Excel file will be automatically opened after the script has finished running.

### ![Reddit](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)
1. Clone this repository or download the script to your local machine.
2. Create a [Reddit Script app](https://www.reddit.com/prefs/apps) and get your credential and secret.
3. Open the script in a Python IDE or text editor.
4. Run the script and enter the required inputs in the command prompt when prompted:
    - The subreddit name you want to scrape
    - The number of posts you want to scrape
    - The name of the CSV file to be stored
5. The script will start scraping posts and store them in an CSV file with the specified name.
6. The CSV file will be automatically opened after the script has finished running.

## Functionality and Features
- The program scrapes a specified number of tweets containing a particular keyword from Twitter and a specified number of posts from a subreddit on Reddit.
- The scraped tweets/posts are stored in an Excel or CSV file.
- The program uses the Selenium web driver to automate the process of logging in to Twitter (if required) and searching for tweets.
- The program prompts the user to enter their Twitter login credentials (if required) and the number of tweets they want to scrape (if they want to scrape Twitter).
- The program allows the user to specify the keyword they want to search for (if they want to scrape Twitter), the subreddit they want to scrape (if they want to scrape Reddit), and the name of the Excel or CSV file to be stored.

## Where to Contribute?

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220327234835/How-to-Contribute-to-Open-Source-Projects-on-GitHub.png" alt="Scraping Twitter" width="512" height="220" />

Contributions to this project are welcome! In addition to improving the existing Twitter and Reddit scrapers, there are opportunities to develop similar scripts for other social media websites such as Facebook, Instagram, and more.

If you're interested in contributing, here are some ideas:

- Develop a scraper for a different social media website
- Improve the existing Twitter/Reddit scraper by adding new features or optimizing performance
- Create a user-friendly UI for the scraper ✅
- Add support for scraping multimedia content such as images and videos
- Implement natural language processing techniques to analyze the scraped content

To contribute, you can fork the repository, make your changes, and submit a pull request. Before making any major changes, please create an issue to discuss your proposed changes with the project maintainers.

We appreciate any contributions to this project and look forward to seeing what the community can create!

## How to Contribute
Contributions to this project are always welcome! If you would like to contribute, please follow these steps:

1. Fork the repository
2. Clone the repository to your local machine
3. Create a new branch for your feature or bug fix
4. Make your changes and commit them with descriptive commit messages
5. Push your changes to your fork
6. Create a pull request to the main repository

## License
This project is licensed under the MIT License - see the LICENSE file for details. By contributing to this project, you agree that your contributions will be licensed under its MIT License.
