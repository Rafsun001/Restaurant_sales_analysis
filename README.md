# Analyze Restaurant Sales Data
Restaurant sales data is collected from kaggle. Various techniques are applied and various graphs are also created to solve some queries.

## Tools used:
1. Python
2. Pandas
3. Numpy
4. Matplotlib
5. Seaborn
6. Scikit-learn

## Solved Queries:
**Query 1:** What is the total sold quantity of a specific product during a particular time period?

![Query 1 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q1.png?raw=true )

The graph illustrates the sales trends of various food items across different times of the day. Cold coffee emerged as the top-selling item during the night and morning hours. Sugarcane juice dominated sales during the afternoon, while panipuri was the primary choice in the evening. At midnight, aalopuri and vadapav were the most popular items, indicating a higher demand during that time. Hence, adjusting production to meet these demands at respective times seems prudent. Conversely, vadapav experienced the lowest sales during the night, while sandwiches lagged in the afternoon. Aalopuri had reduced demand in the evening, and frankie sales were notably low during morning and midnight hours. Considering these patterns, a strategic shift in production to align with demand fluctuations would be beneficial.


**Query 2:** What was the total sales amount of items during a particular time period?

![Query 2 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q2.png?raw=true)

**Query 3:** What was the quantity of a specific product sold on a particular day?

![Query 3 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q3.png?raw=true )

**Query 4:** How much sales revenue was generated from each item for each day?

![Query 4 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q4.png?raw=true )

The sales data for a week indicates the following trends:
On Saturday, the highest revenue was from cold coffee, totaling $800, while the lowest was from vadapav, amounting to $1920.
Sunday witnessed sandwich sales leading with $8460, whereas vadapav sales were the lowest at $3260.
Monday showed a significant spike in sandwich sales at $13380, while vadapav sales remained at $3260.
Tuesday's top seller was the sandwich, generating $8280, and the least revenue came from panipuri, totaling $1680.
Wednesday continued the trend with sandwich sales reaching $9840 and aalopuri sales at a lower $1620.
Thursday sustained sandwich sales dominance at $8460, while aalopuri sales amounted to $3960.
Friday maintained sandwich sales dominance with $9240, while vadapav sales were the lowest at $1360.
   
**Query 5:** Calculate the total quantity of items sold within a specific time frame?

![Query 5 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q5.png?raw=true )

The graph indicates that the highest volume of sales occurred during the night and afternoon, while the lowest sales were recorded in the morning. On average, sales were consistent in the evening and morning periods.
    
**Query 6:** Calculate the total quantity of items sold each day?

![Query 6 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q6.png?raw=true )

The sales data indicates a notable peak in transactions on Monday, reaching a quantity of 160 units, while Saturday marked the lowest sales at 125 units. Following Monday, Sunday and Thursday witnessed the second and third-highest sales, hitting quantities of 155 and 150 units, respectively. Surprisingly, Tuesday appeared to hover around the average with sales amounting to 146 units. The sales trend appears to favor the beginning of the week, with Monday taking the lead. This pattern might suggest a tendency for higher consumer activity or promotions coinciding with the start of the week. Conversely, the weekend, particularly Saturday, seemed to exhibit a dip in sales, which could indicate various factors, such as  differing consumer behaviors during weekends.

**Query 7:** What is the total sold amount of each product?

![Query 7 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q7.png?raw=true )

The graph indicates that the sandwich is the highest profit-generating item for the restaurant, raking in an impressive $65,820. Following closely behind are the frankie and cold coffee, bringing in $57,500 and $54,440, respectively. It's fascinating to see how specific menu items can significantly impact revenue. On the flip side, the average profit-maker, the panipuri, amounts to $24,520. It's quite interesting that an item considered average still brings in a substantial profit. However, the aalopuri and vadapav seem to be the least profitable items, only earning $20,880 and $20,120. This suggests a potential need to reassess these menu choices or explore strategies to boost their popularity and profitability.
   
**Query 8:** How frequently has each item type been purchased or sold?

![Query 8 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q8.png?raw=true )

The graph illustrates a significantly higher volume of fast food sold by the restaurant in comparison to beverages, with quantities reaching 680 units for fast food and 340 for beverages. It's quite evident that the demand for fast food outstrips that of beverages by a considerable margin.
    
**Query 9:** How many orders were received by male and female?

![Query 9 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q9.png?raw=true )

In the realm of food deliveries, there seems to be a prevalence of male recipients over their female counterparts. The statistics indicate a notable discrepancy, with approximately 540 deliveries being made to male recipients, while around 480 deliveries have been received by females. This data unveils an intriguing pattern that leans toward a higher frequency of deliveries to male individuals.
    
**Query 10:** What was the most frequently utilized transaction method?

![Query 10 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q10.png?raw=true )

The graph strikingly illustrates a significant preference for cash transactions over online methods, with around 580 payments made in cash compared to 440 via online channels. This data strongly indicates a prevailing reliance on physical currency despite the growth of digital payment options. 
    
**Query 11:** How frequently was each transaction method used at different times?

![Query 11 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q11.png?raw=true )
    
**Query 12:** How many transactions were conducted each day for each payment method?

![Query 12 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q12.png?raw=true )
    
**Query 13:** What is the total sold amount of each month?

![Query 13 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q13.png?raw=true )

Looking at this graph, it's crystal clear that January was the reigning champ with sales hitting a whopping 29,000 USD! It was the superstar month, outshining the others by a significant margin. On the flip side, April and June were the underdogs, trailing at around 17,000 USD each. October and May emerged as the surprise contenders for second and third place, not too far behind January, raking in 27,000 USD and 28,000 USD, respectively. They really gave the top spot a run for its money! February and March seemed to chill in the middle, boasting an average performance with sales hovering around 26,000 USD. They played it steady, neither stealing the show nor lagging behind.
    
**Query 14:** What is the total sold amount of each time period?

![Query 14 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q14.png?raw=true )

The graph illustrates that the highest profitability was recorded during the nighttime, amounting to approximately 62,075 USD, whereas the least profitable period was observed at midnight, generating around 51,000 USD. On average, the evening and morning periods yielded profits of approximately 52,355 USD and 53,730 USD, respectively. From a formal perspective, the data delineates a clear trend where nighttime emerges as the peak profit-generating period, while midnight notably shows a dip in profitability. The average profits during the evening and morning times suggest a relatively consistent yet slightly higher profit margin during the morning hours.
    
**Query 15:** What is the total sold amount of each item?

![Query 15 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q15.png?raw=true )
    
**Query 16:** What is the total sold amount of each item type?

![Query 16 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q16.png?raw=true )

The graphical representation highlights a substantial revenue discrepancy among items sold, with sandwiches emerging as the top revenue-generating item, amassing approximately 65820 USD. Conversely, vadapav, aalopuri, and panipuri lagged significantly behind, yielding 20120 USD, 20880 USD, and 24520 USD, respectively, depicting notably lower sales figures. Interestingly, following the robust performance of frankie and cold coffee emerged as the subsequent high revenue generators, contributing around 57500 USD and 54440 USD, respectively. This data underscores the clear disparity in consumer preference and demand across the items offered. From a formal standpoint, it is evident that certain items, such as sandwiches, exhibit markedly higher appeal and commercial viability compared to others like vadapav, aalopuri, and panipuri. 

**query 17:** Create a lineplot and show total sell of each month

![Query 17 image](https://github.com/Rafsun001/Restaurant_sales_analysis/blob/main/images/q17.png?raw=true )
