# Election_Analysis

## Overview
 The purpose of this challenge was to utilize python to process election data from a .csv file and analyze the results. In order to complete this project, the goal was to utilize for loops as well as conditional statements to create a program that would read through the csv file, count votes for each candidate (and county) and print the results. The assignment also required the results be written into a text file. 
  
## Election Audit Results 

![electionresult_img](https://github.com/kaileyosha/Election_Analysis/blob/main/Election_Analysis/electionresult_img.png)

  The results of the election audit are shown above, a screencap from the text file. The important things to note are as follows: 
    * Jefferson County had a 10.5% voter turnout with a total of 38,855 people in the county voting.
    * Denver County had the largest voter turnout at 82.8% and 306,055 people voting. 
    * Apache County had the smallest voter turnout at 6.7% which translates to 24,801 people voting. 
    * The clear winner with an overwhelming majority vote of 73.8% or 272,892 votes was Diana DeGette. 
    * The least popular candidate was Raymon Anthony Doane with only 11,606 votes or 3.1% of total votes. 
    * Charles Casper Stockham was the runner up in the election with 23% of the vote or 85,213 votes. 

## Election Audit Summary 
  The code was made to be generally broad, allowing for it to be adapted across elections. For example, the code pertaining to candidates could be easily modified to track ammendments being voted on. All that would need to be done is changing the variables pertainint to candidates to ammendments, the vote vounter for ammendments could for simplicity only count those who voted in favor of the ammendment, or two vote counters could be created (one for those in favor, one for those not in favor.) From there, the county trackers could be modified to count the votes for and against by county to see which counties favored the ammendment and which did not. Another easy change would be to adapt the code to local elections, simply eliminating the county variables and the code could easily run county-wide or even city-wide elections and determine the winnner, such as mayor of a city, or a new schoolboard member in a given county. 

