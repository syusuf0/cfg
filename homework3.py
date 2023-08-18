#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')


# In[5]:


#Question 1 

titanic = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
sex_counts = titanic['sex'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Proportion of Male/Female Passengers')
plt.show()


# In[14]:


#Question 2

plt.figure(figsize=(10, 6))
plt.scatter(titanic['age'], titanic['fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Relationship Between Age and Fare')
plt.show()


### Interpretation
#The scatter plot depicts the correlation between the age and fare variables within the population of Titanic passengers. Based on the analysis of the plot, it can be shown that there is a lack of a significant link between age and fare, as the data points exhibit a scattered distribution without displaying a discernible pattern. However, it is possible to observe some clusters of data points, suggesting that particular age groups may have exhibited a greater inclination to pay specific fare levels.


# In[11]:


#Question 3 
plt.figure(figsize=(12, 6))
sns.barplot(data=titanic, x='class', y='survived', hue='sex', ci=None)
plt.title('Survival Ratio by Class and Sex')
plt.ylabel('Survival Ratio')
plt.show()


# In[13]:


### Interperatation:

#The survival rates of first-class passengers tend to be higher in comparison to those of second and third-class passengers.
#The survival rates of female passengers are consistently greater than those of male passengers across all passenger classifications.


# In[ ]:




