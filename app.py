#python -m streamlit run app.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
# yfinance is imported to scrape data from yaho finance

#from keras.models import load_model
import streamlit as st
#import tensorflow.compat.v2 as tf

def load_data(file_path):
    return pd.read_csv(file_path)
df=load_data('restaurant_sales_for_report.csv')

st.title('Restaurant data analysis report')
st.write(df.head())




st.header("Query 1: What is the total sold quantity of a specific product during a particular time period?")
fig1=plt.figure(figsize=(10,6))
sns.countplot(data=df, x='item_name', hue='time_of_sale')
plt.xlabel("Item name")
plt.ylabel("Total Quantity")
plt.title("Total sell quantity of item  by Time")
plt.legend(title='Selling Time', bbox_to_anchor=(1, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

st.text_area('The graph illustrates the sales trends of various food items across different times of the day. Cold coffee emerged as the top-selling item during the night and morning hours. Sugarcane juice dominated sales during the afternoon, while panipuri was the primary choice in the evening. At midnight, aalopuri and vadapav were the most popular items, indicating a higher demand during that time. Hence, adjusting production to meet these demands at respective times seems prudent. Conversely, vadapav experienced the lowest sales during the night, while sandwiches lagged in the afternoon. Aalopuri had reduced demand in the evening, and frankie sales were notably low during morning and midnight hours. Considering these patterns, a strategic shift in production to align with demand fluctuations would be beneficial.')



sales_by_item_time = df.groupby(['item_name', 'time_of_sale'])['total_price'].sum().reset_index()
st.header("Query 2: What was the total sales amount of items during a particular time period?")
sns.set(style="whitegrid")
fig2=plt.figure(figsize=(12, 6))
sns.barplot(data=sales_by_item_time, x='item_name', y='total_price', hue='time_of_sale')
plt.xticks(rotation=45)  
plt.xlabel("Item name")
plt.ylabel("Total selling amount")
plt.title("Total sold amount of item  by Time")
plt.show()
st.pyplot(fig2)
st.text("")

st.header("Query 3: What was the quantity of a specific product sold on a particular day?")
fig3=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='item_name', hue='DayName')
plt.xlabel("Time of Sale")
plt.ylabel("Count")
plt.title("Count of Item Sales by Time")
plt.legend(title='Item Name', bbox_to_anchor=(1, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)
#st.text("")

total_sales_by_day =df.groupby(['DayName', 'item_name'])['total_price'].sum().reset_index()
pivot_sales = total_sales_by_day.pivot(index='item_name', columns='DayName', values='total_price')
st.header("Query 4: How much sales revenue was generated from each item for each day??")
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 8))
pivot_sales.plot(kind='bar', ax=ax)
ax.set_xlabel('Item Name')
ax.set_ylabel('Total Sales')
ax.set_title('Total Sales of Items at Different Times of Sale')
ax.legend(title='Time of Sale')
ax.set_xticklabels(pivot_sales.index, rotation=45)
plt.tight_layout()
st.pyplot(fig)
que4="""
The sales data for a week indicates the following trends: On Saturday, the highest revenue was from cold coffee, totaling 800 USD, while the lowest was from vadapav, amounting to 1920 USD. Sunday witnessed sandwich sales leading with 8460 USD, whereas vadapav sales were the lowest at 3260 USD. Monday showed a significant spike in sandwich sales at 13380 USD, while vadapav sales remained at 3260 USD. Tuesday's top seller was the sandwich, generating 8280 USD, and the least revenue came from panipuri, totaling 1680 USD. Wednesday continued the trend with sandwich sales reaching 9840 USD and aalopuri sales at a lower 1620 USD. Thursday sustained sandwich sales dominance at 8460 USD, while aalopuri sales amounted to 3960 USD. Friday maintained sandwich sales dominance with $9240, while vadapav sales were the lowest at 1360 USD.
"""
st.text_area(que4)

st.header("Query 5: Calculate the total quantity of items sold within a specific time frame?")
fig5=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='time_of_sale')
plt.xlabel("Time of Sale")
plt.ylabel("Count")
plt.title("Count of Sell in Time")
plt.tight_layout()
st.pyplot(fig5)
st.text_area("The graph indicates that the highest volume of sales occurred during the night and afternoon, while the lowest sales were recorded in the morning. On average, sales were consistent in the evening and morning periods.")

st.header("Query 6: Calculate the total quantity of items sold each day?")
fig6=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='DayName')
plt.xlabel("Time of Sale")
plt.ylabel("Count")
plt.title("Count of Sell in a day")
plt.tight_layout()
st.pyplot(fig6)
st.text_area("The sales data indicates a notable peak in transactions on Monday, reaching a quantity of 160 units, while Saturday marked the lowest sales at 125 units. Following Monday, Sunday and Thursday witnessed the second and third-highest sales, hitting quantities of 155 and 150 units, respectively. Surprisingly, Tuesday appeared to hover around the average with sales amounting to 146 units. The sales trend appears to favor the beginning of the week, with Monday taking the lead. This pattern might suggest a tendency for higher consumer activity or promotions coinciding with the start of the week. Conversely, the weekend, particularly Saturday, seemed to exhibit a dip in sales, which could indicate various factors, such as  differing consumer behaviors during weekends.")

total_sales_by_item =df.groupby(['item_name'])['total_price'].sum().reset_index()
st.header("Query 7: What is the total sold amount of each product?")
sns.set(style="whitegrid")
fig7=plt.figure(figsize=(12, 6))
sns.barplot(data=total_sales_by_item, x='item_name', y='total_price')
plt.xticks(rotation=45)  
plt.xlabel("Item name")
plt.ylabel("Total selling amount")
plt.title("Total sold amount of each item")
st.pyplot(fig7)
st.text_area("The graph indicates that the sandwich is the highest profit-generating item for the restaurant, raking in an impressive $65,820. Following closely behind are the frankie and cold coffee, bringing in $57,500 and $54,440, respectively. It's fascinating to see how specific menu items can significantly impact revenue. On the flip side, the average profit-maker, the panipuri, amounts to $24,520. It's quite interesting that an item considered average still brings in a substantial profit. However, the aalopuri and vadapav seem to be the least profitable items, only earning $20,880 and $20,120. This suggests a potential need to reassess these menu choices or explore strategies to boost their popularity and profitability.")

total_sales_by_item =df.groupby(['item_name'])['total_price'].sum().reset_index()
st.header("Query 8: How frequently has each item type been purchased or sold?")
sns.set(style="whitegrid")
fig8=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='item_type')
plt.xlabel("Item type")
plt.ylabel("Count")
plt.title("Count of Sell of each item type")
plt.tight_layout()
st.pyplot(fig8)
st.text_area("The graph illustrates a significantly higher volume of fast food sold by the restaurant in comparison to beverages, with quantities reaching 680 units for fast food and 340 for beverages. It's quite evident that the demand for fast food outstrips that of beverages by a considerable margin.")


st.header("Query 9: How many orders were received by male and female?")
sns.set(style="whitegrid")
fig9=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='received_by')
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Count of order received by gender")
plt.tight_layout()
st.pyplot(fig9)
st.text_area("In the realm of food deliveries, there seems to be a prevalence of male recipients over their female counterparts. The statistics indicate a notable discrepancy, with approximately 540 deliveries being made to male recipients, while around 480 deliveries have been received by females. This data unveils an intriguing pattern that leans toward a higher frequency of deliveries to male individuals.")

st.header("Query 10: What was the most frequently utilized transaction method?")
sns.set(style="whitegrid")
fig10=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='transaction_type')
plt.xlabel("transaction type")
plt.ylabel("Count")
plt.title("Count of transaction type")
plt.tight_layout()
st.pyplot(fig10)
st.text_area("The graph strikingly illustrates a significant preference for cash transactions over online methods, with around 580 payments made in cash compared to 440 via online channels. This data strongly indicates a prevailing reliance on physical currency despite the growth of digital payment options.")

st.header("Query 11: How frequently was each transaction method used at different times?")
sns.set(style="whitegrid")
fig11=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='time_of_sale', hue='transaction_type')
plt.xlabel("Time of order")
plt.ylabel("Total order count")
plt.title("Transaction method vs time")
plt.legend(title='Transaction type', bbox_to_anchor=(1, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig11)
#st.text("")

st.header("Query 12: How many transactions were conducted each day for each payment method?")
sns.set(style="whitegrid")
fig12=plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='DayName', hue='transaction_type')
plt.xlabel("Day Name")
plt.ylabel("Total order count")
plt.title("Transaction method vs DayName")
plt.legend(title='Transaction type', bbox_to_anchor=(1, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig12)
#st.text("")

total_sales_by_month =df.groupby(['MonthName'])['total_price'].sum().reset_index()
st.header("Query 13: What is the total sold amount of each month?")
sns.set(style="whitegrid")
fig13=plt.figure(figsize=(10, 6))
sns.barplot(data=total_sales_by_month, x='MonthName', y='total_price')
plt.xticks(rotation=45)  
plt.xlabel("MonthName")
plt.ylabel("Total selling amount")
plt.title("Total sold amount in each month")
st.pyplot(fig13)
st.text_area("Looking at this graph, it's crystal clear that January was the reigning champ with sales hitting a whopping 29,000 USD! It was the superstar month, outshining the others by a significant margin. On the flip side, April and June were the underdogs, trailing at around 17,000 USD each. October and May emerged as the surprise contenders for second and third place, not too far behind January, raking in 27,000 USD and 28,000 USD, respectively. They really gave the top spot a run for its money! February and March seemed to chill in the middle, boasting an average performance with sales hovering around 26,000 USD. They played it steady, neither stealing the show nor lagging behind.")

total_sales_by_time =df.groupby(['time_of_sale'])['total_price'].sum().reset_index()
st.header("Query 14: What is the total sold amount of each time period?")
sns.set(style="whitegrid")
fig14=plt.figure(figsize=(10, 6))
sns.barplot(data=total_sales_by_time, x='time_of_sale', y='total_price')
plt.xticks(rotation=45)  
plt.xlabel("time_of_sale")
plt.ylabel("Total selling amount")
plt.title("Total sold amount vs time")
st.pyplot(fig14)
st.text_area("The graph illustrates that the highest profitability was recorded during the nighttime, amounting to approximately 62,075 USD, whereas the least profitable period was observed at midnight, generating around 51,000 USD. On average, the evening and morning periods yielded profits of approximately 52,355 USD and 53,730 USD, respectively. From a formal perspective, the data delineates a clear trend where nighttime emerges as the peak profit-generating period, while midnight notably shows a dip in profitability. The average profits during the evening and morning times suggest a relatively consistent yet slightly higher profit margin during the morning hours.")

total_sales_by_item_nm =df.groupby(['item_name'])['total_price'].sum().reset_index()
st.header("Query 15: What is the total sold amount of each item?")
sns.set(style="whitegrid")
fig15=plt.figure(figsize=(10, 6))
sns.barplot(data=total_sales_by_item_nm, x='item_name', y='total_price')
plt.xticks(rotation=45)  
plt.xlabel("item_name")
plt.ylabel("Total selling amount")
plt.title("Total sold amount vs item name")
st.pyplot(fig15)
st.text_area("The graphical representation highlights a substantial revenue discrepancy among items sold, with sandwiches emerging as the top revenue-generating item, amassing approximately 65820 USD. Conversely, vadapav, aalopuri, and panipuri lagged significantly behind, yielding 20120 USD, 20880 USD, and 24520 USD, respectively, depicting notably lower sales figures. Interestingly, following the robust performance of frankie and cold coffee emerged as the subsequent high revenue generators, contributing around 57500 USD and 54440 USD, respectively. This data underscores the clear disparity in consumer preference and demand across the items offered. From a formal standpoint, it is evident that certain items, such as sandwiches, exhibit markedly higher appeal and commercial viability compared to others like vadapav, aalopuri, and panipuri. ")

total_sales_by_item_typ =df.groupby(['item_type'])['total_price'].sum().reset_index()
st.header("Query 16: What is the total sold amount of each item type?")
sns.set(style="whitegrid")
fig16=plt.figure(figsize=(10, 6))
sns.barplot(data=total_sales_by_item_typ, x='item_type', y='total_price')
plt.xticks(rotation=45)  
plt.xlabel("item_type")
plt.ylabel("Total selling amount")
plt.title("Total sold amount vs item type")
st.pyplot(fig16)
#st.text("")

total_sales_by_month =df.groupby(['MonthName'])['total_price'].sum().reset_index()
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
total_sales_by_month['MonthName'] = pd.Categorical(total_sales_by_month['MonthName'], categories=month_order, ordered=True)
total_sales_by_month = total_sales_by_month.sort_values('MonthName')
st.header("query 17: Create a lineplot and show total sell of each month")
fig17=plt.figure(figsize=(10, 6))
sns.lineplot(x="MonthName",y="total_price",data=total_sales_by_month)
sns.set(style="darkgrid")
plt.xticks(rotation=45) 
st.pyplot(fig17)

st.markdown('## Suggestion')
tr="""
1.Menu Optimization: Reevaluate the menu offerings by considering the sales trends. Items like sandwiches, frankie, and cold coffee are consistent top performers, while vadapav and aalopuri show lower sales and profitability. Consider introducing new variations or marketing strategies for underperforming items to boost their popularity and profitability.

2.Time-based Production: Align production schedules with sales trends during specific times of the day. For instance, adjust production quantities of items like cold coffee for nights and mornings, sugarcane juice for afternoons, and panipuri, aalopuri, and vadapav for evening and midnight hours to meet demand more accurately.

3.Promotions and Marketing: Capitalize on the observed sales patterns, especially the peak on Mondays, to run targeted promotions or campaigns at the beginning of the week. Consider incentivizing weekend sales to counter the observed dip in Saturday sales and potentially attract more customers during these days.

4.Payment Options and Delivery Strategy: Despite the dominance of cash transactions, consider expanding online payment options to cater to changing consumer preferences. Additionally, analyze the demographic trend of more deliveries to male recipients and strategize marketing efforts or menu choices accordingly.

5.Focus on Profitable Hours: Recognize the higher profitability during the night and morning periods. This could involve highlighting or promoting specific items during these hours or adjusting staffing levels to optimize service quality during these profitable times.

6.Seasonal Adjustments: Leverage the insight from the month-wise sales data. Consider seasonal variations in consumer preferences and adjust menu items or promotional activities accordingly. For instance, capitalizing on the popularity of certain items during specific months and offering seasonal specials.
"""
st.text_area(tr)



