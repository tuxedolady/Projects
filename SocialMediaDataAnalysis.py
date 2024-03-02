#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[2]:


# your code here


# In[1]:


get_ipython().system('pip install tweepy')
get_ipython().system('pip install --upgrade pip')
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


categories=['food','Travel','Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']

n=500
Data= { 'Date': pd.date_range(2021-1-1, periods=n),
        'Category': [random.choice(categories) for _ in range(n)],
        'Like': np.random.randint( 0, 1000, size=n)
      }
df= pd.DataFrame(Data)

print("DataFrame Head is:")
print(df.head())

print("\nDataFrame information :")
print(df.info())

print("\nDataFrame description:")
print(df.describe())

print("\ncount of each 'Category'elements:")
print(df['Category'].value_counts())


# In[3]:


df_cleaned=df.dropna()
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned["Date"]=pd.to_datetime(df_cleaned["Date"])
df_cleaned["Like"]= df_cleaned["Like"].astype(int)
print(df_cleaned.head())


# In[14]:


#visualize

sns.histplot(df_cleaned["Like"])
plt.show()

sns.boxplot(x="Category",y="Like", data=df_cleaned)
plt.show()

print("mean of likes:" ,df_cleaned['Like'].mean())
mean_likes_per_category = df_cleaned.groupby('Category')['Like'].mean()
print ("\nmean likes per Category:")
print(mean_likes_per_category)

highest_likes_category = mean_likes_per_category.idxmax()
highest_likes = mean_likes_per_category.max()

print(f"The category with the highest average likes is '{highest_likes_category}' with an average of {highest_likes:.2f} likes.")


# In[ ]:




