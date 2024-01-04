# Growth of the Video Game Industry in the Past Four Decades
Project status - Active 

# Project Objective
This project tackles how video game genres have evolved throught the years utilizing their sales as a metric for their popularity. The objective is to determine whether the Adventure genre has performed differently compared to other genres in the video game industry over the last four decades.

# Methods
The following methods were utilized:
* Filtering 
* Grouping
* Transformation
* Exploratory data analysis (EDA)  
* Visualization

# Technologies
For the purposes of this project, we used the following technologies:
* Python 3.11.5
* MySQL 8.0.34
* Pandas
* Matplotlib.pyplot 
* Seaborn
* Scipy.stats
* Pymysql
* Sqlalchemy
* Getpass

# Project Description
To be able to understand the behaviour of the Adventure video game genre, we utilized two datasets. Our first dataset has 8 columns (Rank, Title, Publisher, Developer, Total Sales, Release Date, Last Update and Genre) and 1,034 rows. It contains the sales data of the video games with the most sales on a global scale, and it ranks them accordingly. Its oldest entry is from 1979 and its most recent entry is from 2023. It has some missing values (9 values for release dates and 24 values for total sales) but overall it is a comprehensive showing of video game sales. 

Our second dataset has 16 columns (Rank, Title, Console, Publisher, Developer, VGChartz Score, Critic Score, User Score,	Total Sales,	NA Sales,	PAL Sales,	Japan Sales,	Other Sales,	Release Date,	Last Update and	Genre) and 54,551 rows. In comparison to the first dataset, this one has more missing values but for the purposes  of our study we chose to ionly keeo the following columns (Title, Console, Total Sales,	NA Sales,	PAL Sales,	Japan Sales and Other Sales). 

The data that is present in these datasets was obtained from https://www.vgchartz.com/gamedb/ via a web scraper.

We obtained our datasets from the following source: https://www.kaggle.com/datasets/mikegillotti/video-game-sales?select=video+game+sales+titles.csv

# Steps
During our time working with the dataset, we found some new insights and decided to reformulate our original hypothesis to better utilize the information we had available.

# Conclusion
After finishing the analysis, we can say that the Adventure genre has performed differently when compared to the other video game genres and that we can accept our hypothesis. 
