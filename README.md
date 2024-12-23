# ETL-Pipeline-for-Web-Scraping-in-Python Using Multithreading

In this project, I have built an **ETL pipeline** to scrape data from a website, process it, and load it into a database. This project was inspired by **Shiksha Online Courses** (YouTube: [Shiksha Online Courses](https://www.youtube.com/@ShikshaOnlineCourses)). The goal was to automate the extraction of data from a web page, process it efficiently, and store the cleaned data in a relational database system using Python and multithreading.

## Tools Used
- **Python Libraries:**
  - `requests` and `requests-html` for sending HTTP requests and retrieving web content
  - `BeautifulSoup` for parsing HTML content and extracting required data
  - `pandas` for handling and processing data
  - `re` module for regex pattern matching to clean and filter data
  - `sqlite3` for interacting with the SQLite database
  - `concurrent.futures` for implementing multithreading
- **Design Paradigms:**
  - Object-Oriented Programming (OOP)
  - Multithreading for scaling the ETL pipeline

## Design Architecture
I designed an **ETL class** that encapsulates the logic for a particular web page's extraction, transformation, and loading process. The architecture focuses on the following steps:
1. **Extract**: Retrieve the data from the target website using web scraping techniques.
2. **Transform**: Clean the extracted data and perform necessary transformations.
3. **Load**: Store the processed data in a relational database (SQLite in this case).

Once the extraction logic for each page was ready, I scaled up the ETL process using **multithreading**. By creating an object of the ETL class for each page, I could run multiple ETL pipelines concurrently, thus speeding up the overall process. The `concurrent.futures.ThreadPoolExecutor` was used to efficiently manage threads and execute tasks concurrently.

## Learnings from This Exercise
During this project, I gained valuable experience in several areas:
- **Web Scraping and Website Inspection**: I learned how to inspect web pages, identify the structure of HTML, and scrape the necessary data.
- **Multithreading**: I explored how to run multiple threads concurrently to handle multiple tasks (in this case, scraping and processing multiple pages) at once.
- **ETL Building**: I implemented a complete ETL pipeline that automates the process of extracting, transforming, and loading data.
- **Object-Oriented Programming (OOP)**: I encapsulated the ETL logic in an OOP manner, making the code modular and reusable.
- **`functools.partial`**: I used this function to create customized versions of functions and handle arguments in a cleaner way.
- **Storing Data in an RDBMS**: I gained practical experience in using SQLite to store processed data in a database.
- **Regex Pattern Building**: I learned the basics of using regular expressions to clean and extract specific data from text.

## References
1. [NHAI list of Toll Plazas](https://tis.nhai.gov.in/tollplazasataglance.aspx?language=en#)
2. [NHAI Rate Page for a Plaza](https://tis.nhai.gov.in/TollInformation.aspx?TollPlazaID=99)
3. [functools' official documentation](https://docs.python.org/3/library/functools.html#partial)
4. [concurrent module](https://docs.python.org/3/library/concurrent.futures.html)
5. [Regex module preliminary](https://www.w3schools.com/python/python_regex.asp)
6. [Regex module official documentation](https://docs.python.org/3/library/re.html)
7. [curl to code converter](https://curlconverter.com/)

## Walkthrough
For a more in-depth explanation of how the ETL pipeline was built, including coding techniques and real-time demonstrations, check out the walkthrough video:

[![Webscraping ETL Pipeline in Python](https://yt-embed.herokuapp.com/embed?v=juMlqaPUgRo)](https://youtu.be/juMlqaPUgRo "Webscraping ETL Pipeline in Python")

This video covers everything from setting up the environment to running the multithreaded ETL pipeline.