# sentiment
- Topic: Customer Feedback
- This experiments Prompt Engineering from API OPEN AI to get inferencing (sentiment) and summary for User Feedback on Products 

### Dataset and Model
- Women Clothing Review from Kaggle: https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews
- Amount of dataset: 1200 rows
- Model applied for Prompt Engineering: gpt-turbo-3.5
- For visualizing, timeframe is added with purpose to explore more metrics on PowerBI related to the Customer Feedback

### Expected Result from Prompt
This include 2 seperate process: Prompt Engineering and Data Prep
#### Prompt Engineering part
Based on review_text column, create a dataframe with 4 columns: 
- Department: define 5 departments Marketing, Sales, Product, Logistics, and Inventory to categorize the reviews of customers
- sentiment: positive or negative
- emotions: extract 5 most relevant emotions
- summary: summarize the text within 10 words

#### Data Prep
After prompt engineering is done, we will merge the result into dataset.
Lately, adding timeframe to dataset

### Visualization
Using PowerBI for visualizing the insight and metrics


