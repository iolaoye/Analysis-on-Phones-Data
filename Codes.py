#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[43]:


df=pd.read_csv("C:\\Users\\debo_\\Desktop\\ProjectsData\\best-selling-mobile-phones.csv")


# In[44]:


#Data Exploration 


# In[45]:


df.dtypes


# In[46]:


#Which column has no missing values? Provide a set of column names that have no missing values
np.sum(df.isnull())


# In[47]:


status_val1=df.model.value_counts()
status_val1.head(50)


# In[48]:


#Begin to answer Question 1
#Find the total number of phones sold by various manufacturers


# In[49]:


#Sum the units sold by the different manufacturer group and reset the index
df_Manufacturer=df.groupby(['manufacturer'])['units_sold_m'].sum().reset_index()
df_Manufacturer


# In[50]:


plt.figure(figsize=(10,5))
chart=sns.barplot(x="manufacturer",y="units_sold_m",data=df_Manufacturer)
sns.set_theme(style="whitegrid")
plt.xlabel('Manufacturer', fontsize=18);
plt.ylabel('Total Units Sold (mil)', fontsize=18);
plt.title('Total Units of Mobile Phones Sold by Manufacturers', fontsize=20)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right',fontweight='light',
    fontsize=14)
plt.show()


# In[51]:


#Begin to answer question 2
#Which manufactural sold highest number of Touchscreen? which sold highest number of bar phones?


# In[52]:


#Group the data by form and extract all Touchscreen phones
df_form = df.groupby('form')
df_Touchscreen=df_form.get_group('Touchscreen')
df_Touchscreen


# In[53]:


#Sum the units of Touchscreens (df_Touchscreen) sold by the different manufacturer group and set the result to dataframe
df_Touch_sum=df_Touchscreen.groupby(['manufacturer'])['units_sold_m'].sum().reset_index()
df_Touch_sum


# In[54]:


plt.figure(figsize=(10,5))
chart=sns.barplot(x="manufacturer",y="units_sold_m",data=df_Touch_sum)
sns.set_theme(style="whitegrid")
plt.xlabel('Manufacturer', fontsize=18);
plt.ylabel('Total Units of Touchscreen Sold (mil)', fontsize=18);
plt.title('Total Units of Touchscreen Phones Sold by Manufacturers', fontsize=20)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right',fontweight='light',
    fontsize=14)
plt.show()


# In[55]:


#No. 2a. Apple sold highest number of Touchscreens at 1541.9 million 


# In[56]:


#Begin to answer No 2b. which sold highest number of bar phones?
#Get all Bar phones from the groupby 'form' above
df_Bar=df_form.get_group('Bar')
df_Bar


# In[57]:


#Sum the units of Bar (df_Bar) sold by the different manufacturer group and reset the indesx
df_Bar_sum=df_Bar.groupby(['manufacturer'])['units_sold_m'].sum().reset_index()
df_Bar_sum


# In[58]:


plt.figure(figsize=(10,5))
chart=sns.barplot(x="manufacturer",y="units_sold_m",data=df_Bar_sum)
sns.set_theme(style="whitegrid")
plt.xlabel('Manufacturer', fontsize=18);
plt.ylabel('Total Units of Bar Phones Sold (mil)', fontsize=18);
plt.title('Total Units of Bar Phones Sold by Manufacturers', fontsize=20)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right',fontweight='light',
    fontsize=14)
plt.show()


# In[59]:


#No.2b. Nokia sold highest number of Bar Phones at 2032.84 million


# In[60]:


#Begin to answer question 3. Which manufacturer sold highest number of Smartphones?


# In[61]:


#Group the data by smartphone and extract'YES'
df_smart = df.groupby('smartphone')
df_smart
df_smart_sum=df_smart.get_group('Yes')
df_smart_sum.head(50)


# In[62]:


#Sum the the units_sold in the smartphones dataframe by manufacturer
df_smart_sum_manu = df_smart_sum.groupby(['manufacturer'])['units_sold_m'].sum().reset_index()
df_smart_sum_manu_sort = df_smart_sum_manu.sort_values(['units_sold_m'], ascending=[0])
print(df_smart_sum_manu_sort)


# In[63]:


plt.figure(figsize=(10,5))
chart=sns.barplot(x="manufacturer",y="units_sold_m",data=df_smart_sum_manu)
sns.set_theme(style="whitegrid")
plt.xlabel('Manufacturer', fontsize=18);
plt.ylabel('Total Units of Smartphones Sold (mil)', fontsize=18);
plt.title('Total Units of Smartphones Sold by Manufacturers', fontsize=20)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right',fontweight='light',
    fontsize=14)
plt.show()


# In[64]:


#Apple sold the highest number of smartphones at 1541.9 million


# In[65]:


#Begin to answer question 4
#In which year was the most phones sold?
#Group the data by year and sum the units sold
df_year = df.groupby(['year'])['units_sold_m'].sum().reset_index()
print(df_year)


# In[66]:


#sort the rows in ascending
df_year_sort = df_year.sort_values(['units_sold_m'], ascending=[0])
df_year_sort


# In[67]:


#No.3. Most phones were sold in 2003


# In[68]:


plt.figure(figsize=(10,5))
chart=sns.barplot(x="year",y="units_sold_m",data=df_year_sort)
sns.set_theme(style="whitegrid")
plt.xlabel('Year', fontsize=18);
plt.ylabel('Total Units of Phones Sold (mil)', fontsize=18);
plt.title('Total Units of Phones Sold by Year', fontsize=20)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right',fontweight='light',
    fontsize=14)
plt.show()


# In[69]:


#Begin to answer question 5.
#5. In which year was the most phone models launched?
#Group the data by year and model, then count the models
df_most_model=df.groupby(['year', 'model']).agg(model_count = ('model', 'count'))
df_most_model.head(50)


# In[70]:


#Compute the sum of model_count for each year
df_mm_count = df_most_model.groupby(['year'])['model_count'].sum().reset_index()
df_mm_count


# In[71]:


df_mm_count.model_count.max()


# In[72]:


plt.figure(figsize=(10,5))
chart=sns.barplot(x="year",y="model_count",data=df_mm_count)
sns.set_theme(style="whitegrid")
plt.xlabel('Year', fontsize=18);
plt.ylabel('Total Models of Phones Sold (mil)', fontsize=18);
plt.title('Total Models of Phones Sold by Year', fontsize=20)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right',fontweight='light',
    fontsize=14)
plt.show()


# In[73]:


#Most phone models were launched in 2019 with a total of 18 models

