# Sentiment Analysis on Data Analysis Tools using Twitter API & Python

## Project Overview

This project encompasses the analysis of sentiments expressed in tweets concerning various Data Analysis Tools, namely Python, Power BI, and Excel, using the Twitter API and Python for data processing and analysis.

## Table of Contents

- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Cleaning](#data-cleaning)
- [Sentiment Analysis](#sentiment-analysis)
- [Data Storage](#data-storage)
- [Data Visualization](#data-visualization)
- [Conclusions](#conclusions)

## Introduction

Sentiment analysis, a pivotal aspect of text analysis, facilitates the deciphering of emotions, attitudes, and opinions embedded in textual data. Applied across diverse domains like marketing and politics, this project specifically delves into analyzing sentiments towards data analysis tools: Python, Power BI, and Excel, encapsulated in a collection of tweets.

## Data Collection

Utilizing the Twitter API, tweets pertinent to the data analysis tools of interest were amassed, forming the foundational dataset for our sentiment analysis journey.

## Data Cleaning

Engaged in a meticulous data cleaning process, employing Regular Expressions to purify the tweets by:
- Eradicating URLs
- Omitting mentions and retweets
- Removing irrelevant or duplicate entries

## Sentiment Analysis

Leveraged the TextBlob library, a simplistic API for natural language processing in Python, to perform sentiment analysis on the cleaned data. The sentiments were categorized as:
- Positive
- Negative
- Neutral

## Data Storage

Enacted procedures for systematically storing the analyzed data into a database, ensuring optimal organization and retrieval functionality for future analysis and visualization.

## Data Visualization

Utilized data visualization libraries, Matplotlib and Seaborn, to create:
- Bar charts reflecting sentiment distributions
- Time-series plots elucidating sentiment evolution over time and across different categories.

## Conclusions

Our analysis revealed some interesting insights. We found that the majority of tweets were neutral and positive in sentiment, while a smaller proportion were negative. We also found that sentiment varied across different categories, with some categories having a higher proportion of tweets than the others. Specifically, Power BI is first with a percentage of 68.7%, second is Excel with a percentage of 23.2% and last is Python with a percentage of 8.1%.
The study also found that the tweet frequency varied throughout the period, with some days having more tweets than others. This could be due to various factors such as new releases, trending topics, or events related to the categories. The study has several limitations, including the small sample size and the reliance on Twitter data, which may not be representative of the general population. Future studies could use a larger sample size and explore other sources of data to validate the findings. Overall, our sentiment analysis of tweets provided valuable insights into the emotions, attitudes, and opinions expressed in tweets related to our topic of interest.



