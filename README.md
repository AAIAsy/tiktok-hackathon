# Introduction

This repo is created for a hackathon challenge by TikTok. The process from getting raw review data and metadata to model training and data analysis will be discussed in the following sections.

## Overview

### Problem statement

The following is the problem statement provided by the organizing party, TikTok:

Online reviews play a crucial role in shaping public perception of local businesses and locations. However, the presence of irrelevant, misleading, or low-quality reviews can distort the true reputation of a place. With the proliferation of user-generated content, ensuring the quality and relevancy of reviews is more important than ever. This hackathon challenges students to leverage Machine Learning (ML) and Natural Language Processing (NLP) to automatically assess the quality and relevancy of Google location reviews, aligning them with a set of well-defined policies. The ultimate goal is to improve the reliability of review platforms and enhance user experience.


### Objectives

Tiktok has outlined clear objectives that should be met by the end of the 72-hour hackathon challenge:

- Gauge review quality: Detect spam, advertisements, irrelevant content, and rants from users who have likely never visited the location.
- Assess relevancy: Determine whether the content of a review is genuinely related to the location being reviewed.
- Enforce policies: Automatically flag or filter out reviews that violate the following example policies:
  - No advertisements or promotional content.
  - No irrelevant content (e.g., reviews about unrelated topics).
  - No rants or complaints from users who have not visited the place (can be inferred from content, metadata, or other signals).


# Process

The team has employed the following strategies from data collection to training a BERT model for classification.

## Data collection

The data was collected by downloading review and business metadata files from the Google Local Reviews dataset page. Five (5) files of these types were downloaded and are later processed using Apache PySpark framework, which allows for distributed processing of very large datasets. Following joining operations between review and metadata datasets and dropping null values to retain authenticity, we have accumulated a huge amount of data numbering 2,528,648 records. The format of the datasets are as follow:

```
customer review dataset format:

user_id - ID of the reviewer
name - name of the reviwer
time - time of the review (unix time)
rating - rating of the business
text - text of the review
pics - pictures of the review
resp - business response to the review including unix time and text of the response
gmap_id - ID of the business


business metadata dataset format:
name - name of the business
address - address of the business
gmap_id - ID of the business
description - description of the business
latitude - latitude of the business
longitude - longitude of the business
category - category of the business
avg_rating - average rating of the business
num_of_reviews - number of reviews
price - price of the business
hours - open hours
MISC - MISC information
state - the current status of the business (e.g., permanently closed)
relative_results - relative businesses recommended by Google
url - URL of the business
```



## Data cleaning and processing

The data was cleaned by removing null values and columns with large number of null values. It is then processed by tokenizing, checking their spelling, removing stopwords, lemmatizing them to root words, normalizing and embedding them for ease of operations for PySpark.

## Data Labelling

The reviews are labelled manually by using methods like cosine similarity for relevancy, pattern searching for promotional/advertising content and sentiment analysis for ranting reviews.

## Model setup and evalutaion

After preprocessing, the data goes through a pipeline to be converted into document and tokenized into sentence-level BERT embeddings. Model training parameters are set up to take in embeddings and output a label for 10 training cycles, following which it will be evaluated with accuracy, F1, precision and recall. 

## Dataset EDA

TF-IDF is used to see how important words are in each dataset. 


# Setup

The notebook can be run on a local machine, but the installation process is very complicated for both Mac and Windows. The simplest way to start setting the project up is download the to your local machine and uploading it on Google Colab.

1. Download any number of review and metadata files in the Google Local Reviews dataset page. and 
2. Click on "Runtime" on the top toolbar and select CPU runtime, as GPU is not needed. Upload the files to Google Colab.
3. Create a folder called "datasets", and inside it, create "review_data" and "review_metadata" sub-folders. Store the appropriate files into their appropriate folders.
4. Run the first cell to install Apache PySpark and Spark NLP frameworks.
5. Run each cell afterwards to run the whole program.



# Limitations

There are some limitations to take note of:
1. the threshold for relevancy is not a universal number, so they are statisitcally calculated to determine what number to be considered low and high for irrelevant and relevant separation.
2. following data preprocessing, we have obtained 0 records for RANT WITHOUT VISIT label, and this is due to using statistics to label rather than manual labelling due to large amounts of data and time-cosuming to do so.
3. the model is confused between RELEVANT and IRRELEVANT labels due to overlapping words that belong to those categories upon TF-IDF inspections.
4. `gpt-4o-mini` was used to aid in labelling through few-shot examples, but after thorough analysis, the model did not correctly label the reviews as per instructions, thus skewing almost all reviews as RELEVANT. 



