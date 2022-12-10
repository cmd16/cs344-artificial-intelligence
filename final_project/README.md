# Exploring spaCy's TextCategorizer on Yelp Restauarant Reviews

## Vision
- Learn how spaCy (a production tool for NLP) can be used to categorize text
- evaluate the performance of various models of text categorization

## How to run the code
- The entirety of the code is contained in `yelp_reviews.ipynb`. That file also contains comments on the results.

### How to get the data
- The dataset was obtained as an SQL database from (https://www.yelp.com/dataset), 
then the steps in this file were performed (https://rpruim.github.io/ds303/S20/from-class/YELP/yelp_eda.html), 
then I saved the `random_reviews` object to a csv file that I called Yelp_restaurant_reviews.csv.
- However, you could run this with other review data. 
As long as you have a csv that has a column for "text" and a column for "stars" (where stars are inbetween 1 and 5), 
all you need to change is the filename. (If the rows are not in random order you'll also want to randomize the order of rows.)

## Where to read the report
- `report.ipynb` contains the final report
