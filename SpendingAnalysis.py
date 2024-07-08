#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[189]:


df = pd.read_csv(r"C:\Users\manny\Documents\PersonalSpendingProj\MonthlyExp.csv")


# In[190]:


print(df.head())


# In[191]:


columns_to_convert = df.columns[3:]  # All columns except the first three

df[columns_to_convert] = df[columns_to_convert].replace('[\$,]', '', regex=True).astype(float)


# In[192]:


print(df)


# In[193]:


print(df.dtypes)


# In[194]:


#Q1 & Q2

#convert to float for all columns except 'Expense', 'Type', and 'TypeID'
columns_to_convert = df.columns[3:]

# Sum the expenses for each category sorted in ascending order
category_sums = df.groupby('Type')[columns_to_convert].sum().sum(axis=1).sort_values(ascending = False)

#print the total spent across 2 years for all expense types
print(category_sums)

# Identify the category with the highest total expense
max_expense_category = category_sums.idxmax()
max_expense_amount = category_sums.max()

print(f"The category with the highest total expense across the 2 years is '{max_expense_category}' with a total of ${max_expense_amount:.2f}.")


# In[195]:


#Q3
Type_name = 'Food'
expense_data = df[df['Type'] == Type_name][columns_to_convert].sum().T

print(expense_data)


# In[196]:


plt.figure(figsize=(10, 6))
plt.bar(expense_data.index, expense_data.values.flatten())
plt.xlabel('Month')
plt.ylabel('Amount Spent ($)')
plt.title(f'Money Spent on {expense_name} Over Time')
plt.xticks(rotation=90)
plt.show()


# In[197]:


#Q4
Pie_Title = df['Type'].unique()
#index = [0,1]
New_PT = np.delete(Pie_Title, 0 )
#Pie_Title.drop(column = 'Housing')
print(Pie_Title)
print(New_PT)
print(category_sums)


# In[199]:


plt.figure(figsize=(15, 12))
plt.pie(category_sums, labels=Pie_Title, autopct='%1.1f%%',  textprops={'fontsize': 14},startangle=140)
plt.title('Percentage of Total Spending by Category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[201]:


# Eliminationg housing which is relatively fixed over time we have this
plt.figure(figsize=(15, 12))
plt.pie(category_sums[1:], labels=New_PT, autopct='%1.1f%%',  textprops={'fontsize': 14},startangle=140)
plt.title('Percentage of Total Spending by Category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[202]:


#Q5
# Transposing the DataFrame for easier plotting
df_T = Total_Per_Month.T

if 'Percentage' in df_T.index:
    df_T = df_T.drop('Percentage', axis=0)
    
# Plotting a line plot for each expense category over the months
plt.figure(figsize=(14, 8))

# Loop over each category and plot its expenses over time
for Type in df_T.columns:
    #print(Type)
    plt.plot(df_T.index, df_T[Type], label=Type)

# Show the line plot 
plt.xlabel('Month')
plt.ylabel('Amount Spent')
plt.title('Monthly Expenses for Each Category Over 2 years')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# In[203]:


#Now let's remove Housing and food as I've analysed my expenses relating to food and my expenses on Housing remained relativly the same.

# Plotting a line plot for each expense category over the months
plt.figure(figsize=(14, 8))

# Loop over each category and plot its expenses over time
for Type in df_T.columns:
    if (Type == 'Housing' or Type == 'Food'):
        continue
    plt.plot(df_T.index, df_T[Type], label=Type)

# Show the line plot 

plt.xlabel('Month')
plt.ylabel('Amount Spent')
plt.title('Monthly Expenses for Each Category Over 2 years')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.locator_params(axis='y', nbins=25)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()







