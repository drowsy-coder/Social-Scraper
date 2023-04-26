# Twitter Scraper

<img src="https://website.understandingdata.com/wp-content/uploads/2022/02/scraping-twitter-1024x440.jpg" alt="Scraping Twitter" width="512" height="220" />

## Introduction
This program is a python script that utilizes the selenium web driver to scrape a specified number of tweets containing a particular keyword from Twitter. The scraped tweets are stored in an excel file that can be easily accessed and analyzed.

<img src="https://i.imgur.com/JS9bxEB.png" alt="Scraping Twitter"/>

## Dependencies
To use this program, you need to have the following installed on your system:
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

You can install selenium and pandas using pip, by running the following commands:
```
pip install selenium
pip install pandas
```
## How to Use
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

## Functionality and Features
- The program scrapes a specified number of tweets containing a particular keyword from Twitter.
- The scraped tweets are stored in an Excel file.
- The program uses the selenium web driver to automate the process of logging in to Twitter and searching for tweets.
- The program prompts the user to enter their Twitter login credentials and the number of tweets they want to scrape.
- The program allows the user to specify the keyword they want to search for and the name of the Excel file to be stored.

## Where to Contribute?
Contributions to this project are welcome! In addition to improving the existing Twitter scraper, there are opportunities to develop similar scripts for other social media websites such as Reddit, Facebook, Instagram, and more.

If you're interested in contributing, here are some ideas:

- Develop a scraper for a different social media website
- Improve the existing Twitter scraper by adding new features or optimizing performance
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
