#!/usr/bin/env python
# coding: utf-8

# #importing libraries
# 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('config', 'InlineBackend.print_figure_kwargs={\'facecolor\' : "white"}')
import datetime
import ast
import seaborn as sns


# #import dataset

# In[3]:


movie = pd.read_csv("movie_dataset.csv")


# In[4]:


movie.head(10)


# In[5]:


movie.describe()


# In[6]:


movie.info()


# #Converting to float 

# In[7]:


movie['Budget'] = pd.to_numeric(movie['Budget'],errors='coerce').astype(float)


# In[8]:


movie['Popularity'] = pd.to_numeric(movie['Popularity'],errors='coerce').astype(float)


# In[9]:


movie['Runtime'] = movie['Runtime'].astype(float)


# #Replacing 'nan' with 0

# In[10]:


movie['Budget'] = movie['Budget'].replace(np.nan, 0)


# In[11]:


movie['Popularity'] = movie['Popularity'].replace(np.nan, 0)


# In[12]:


movie['Revenue'] = movie['Revenue'].replace(np.nan, 0)


# #Descriptive Statistics in Runtime

# In[30]:


movie['Runtime'].describe()


# #Descriptive Statistics of Revenue

# In[221]:


movie['Revenue'].describe()


# #Descriptive Statistics in Budget

# In[13]:


movie['Budget'].describe()


# #Production Company

# In[11]:


movie['Revenue'].sum(['Procdctuoi'])


# #Extracting only year in Release_date

# In[13]:


movie['Year'] = pd.to_datetime(movie['Release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)


# #Revenue and Budget

# In[14]:


movie[movie['Budget'].notnull()][['Title', 'Budget', 'Revenue', 'Year','Production_company','Production_country']].sort_values('Revenue', ascending=False).head(10).style.background_gradient(subset=['Budget','Revenue'],cmap='PuBu',axis=None, low=0.50, high=1.0)


# #Which movie made the highest and lowest revenue?
# 

# In[188]:


movie[movie['Revenue'] == movie['Revenue'].max()].sort_values('Revenue', ascending=False).head(1).style.background_gradient(subset=['Budget','Revenue'],cmap='PuBu',axis=None, low=0.50, high=1.0)


# In[192]:


movie[movie['Revenue'] == movie['Revenue'].min()]


# #Top 10 Movies with highest revenue

# In[19]:


movie[['Title','Revenue','Budget','Runtime','Popularity','Year']].sort_values(['Revenue'],
ascending=False).head(10).style.background_gradient(subset=['Revenue','Budget','Runtime','Popularity'],cmap='PuBu',axis=None, low=0.50, high=1.0)


# #Analyze the Revenue

# In[77]:


Revenue_year = (movie[movie['Revenue'].notnull()][['Year','Revenue']].groupby('Year').mean())
Revenue_year.plot(figsize=(5,5))
plt.title("Distribution of Movie Revenue Per Year", color='black')
plt.xlabel("Year", color='black')
plt.ylabel("Revenue",color='black')
plt.show()


# #Which movie made the highest and lowest budget?

# In[176]:


movie[movie['Budget'] == movie['Budget'].max()].sort_values('Budget', ascending=False).head(1).style.background_gradient(subset=['Budget','Revenue'],cmap='PuBu',axis=None, low=0.50, high=1.0)


# #Top 10 movies with Highest Budget

# In[5]:


movie[['Title','Budget','Year']].sort_values(['Budget'], 
ascending=False).head(10).style.background_gradient(subset='Budget',cmap='PuBu',axis=None, low=0.50, high=1.0)


# #Analyze the budget

# In[99]:


Budget_year = (movie[movie['Budget'].notnull()][['Year','Budget']].groupby('Year').mean())
Budget_year.plot(figsize=(15,5), color='blue')
plt.title("Distribution of Movie Budget Per Year", color='black')
plt.xlabel("Year", color='black')
plt.ylabel("Budget", color='black')
plt.show()


# #Which movie are the longest runtime?
# 

# In[177]:


movie[movie['Runtime'] == movie['Runtime'].max()]


# In[220]:


plt.hist(movie['Runtime'].fillna(0) / 50, bins=[1,2,3,4,5,6], color='blue');
plt.title('Distribution of length of film in hours',fontsize=16,color='black');
plt.xlabel('Duration of Movie in Hours',color='black');
plt.ylabel('Number of Movies',color='black');
plt.show()


# #Trend of  movie runtime

# In[209]:


sns.distplot(movie[(movie['Runtime'] < 300) & (movie['Runtime'] > 5)]['Runtime'])
plt.title("Trend of Movie Runtime",color='black')
plt.xlabel('Runtime (minutes)', color='black')
plt.ylabel('Density', color='black')
plt.show()


# #Top 10 Most Popular movies

# In[6]:


movie[movie['Popularity'].notnull()][['Title','Popularity','Year']].sort_values('Popularity',ascending=False).head(10).style.background_gradient(subset='Popularity',cmap='PuBu',axis=None, low=0.50, high=1.0)


# #Number of movie release per year

# In[28]:


Movie_year = movie.groupby('Year')['Title'].count()
Movie_year.plot(figsize=(10,5),color='blue')
plt.title('Movie Release Per Year',color='black')
plt.ylabel('Movie Count', color='black')
plt.xlabel('Year', color='black')
plt.show()


# In[ ]:




