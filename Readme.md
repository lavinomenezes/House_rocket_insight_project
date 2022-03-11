# House Rocket insight project
<i>Para ler o projeto em português [clique aqui](https://github.com/lavinomenezes/House_rocket_insight_project/blob/main/portugues/Readme_portugu%C3%AAs.md)</i>

## Business Problem

Fictitious property buying and selling company where the CEO of the company would like to maximize the company's profit by finding good deals. Was requested to the data science team to analyze the properties portfolio available to purchase and return a list of buying and selling suggestions to attend the CEO’s demand to maximize the profit and reduze the losts.
An online app will be delivered to make it easy the visualization of the analysis result for all those involved in the process, this app will contain:
<ul>
<li>Suggested buying and selling table with the suggested price of selling;</li>
<li>Map to geographic visualization of the properties suggested;</li>
<li>Analysis of the main business hypothesis.</li>
</ul>

>In the end, it will be the profit that the company can make from the suggestion list.

**Dataset overview**


| **Variable** | **Meaning** |
|:----------:|---------|
|id        |Unique ID for each home sold|
|date|Date of the home sale |
|price| Price of each home sold |
|bedrooms| Number of bedrooms |
|bathrooms| Number of bathrooms, where .5 accounts for a room with a toilet but no shower |
|sqft_living| Square footage of the apartments interior living space |
|sqft_lot| Square footage of the land space |
|floors |Number of floors |
|waterfront |A dummy variable for whether the apartment was overlooking the waterfront or not |
|view |An index from 0 to 4 of how good the view of the property was |
|condition |An index from 1 to 5 on the condition of the apartment, |
|grade |An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of |construction and design. |
|sqft_above |The square footage of the interior housing space that is above ground level |
|sqft_basement |The square footage of the interior housing space that is below ground level |
|yr_built |The year the house was initially built |
|yr_renovated |The year of the house’s last renovation |
|zipcode | What zipcode area the house is in |
|lat |Lattitude |
|long |Longitude |
|sqft_living15 |The square footage of interior housing living space for the nearest 15 neighbors |
|sqft_lot15 |The square footage of the land lots of the nearest 15 neighbors |



##  Business Questions 
<ul>
<li>Which properties the company should buy and at what prices ?</li>
<li>What's the best moment to sell the properties after buying ?</li>
</ul>

##  Business Assumptions
<ul>
<li>City region and season of the year both affect the buying and selling prices;</li>
<li>Informations are limited to the range of one year, from may of 2014 to may of 2015;</li>
<li>Properties with incoherence between then numbers of bedrooms and the total area compared to the average by number of rooms will be considered input errors and will be removed;</li>
<li>Properties built before 1995 were considered old;</li>
<li>Properties with grade of 7 will be considered like medium grade and those with 11 to 13 will be considered like high grade;</li>
<li>Properties with condition of 1 to 2 will be considered in bad conditions and those with 4 to 5 in good conditions;</li>


<li>For purchase was considered properties with good condition and price smaller than the median price of the region(zipcode)
The selling price was determined as follows:</li>
 <ul>
<li>If the purchase price is bigger than the region median + seasonality.</li>
 <ul>
 <li>the price of the sale will be equal to the purchase price + 10%</li>
</ul>
<li>If the purchase price is lower than the region median + seasonality.</li>
<ul>
<li>the price of the sale will be equal to the purchase price + 30%</li>
</ul>  
 </ul>
</ul>

## Solution planning
<ul>
 <li>Data collect;</li>
 <li>Data cleaning;</li>
 <li>Data transform;</li>
 <li>Data description;</li>
 <li>Remove data from input error;</li>
 <li>Feature creation:</li>
 <ul>
 <li>month;</li>
 <li>year_month;</li>
 <li>year;</li>
 <li>season;</li>
 <li>house_age;</li>
 <li>basement;</li>
 <li>median_price_zipcode;</li>
 <li>median_price_season.</li>
 </ul>
 <li>Exploratory analysis;</li>
 <li>Hypothesis testing;</li>
 <li>Conclusion of insights;</li>
 <li>Deploy the app in the cloud</li>
</ul>

##  Main business insight
<ul>
<h3><li><strong>Properties with waterfront are 212,42% more expensive on average</strong></li> </h3>

Way more than expected,which was 30%. So it's necessary a bigger investment to add properties with waterfront in the company's portfolio
 
<h3><strong><li>Properties with waterfront have a month-over-month growth bigger than that without</strong></li></h3> 

While the properties without waterfront have a growth of 0.2% a month on average those that have it grow at 4.81%. Despite the bigger investment to purchase properties with waterfront in the medium and long term they can represent a good investment.

<h3><strong><li>Properties with a high grade have a growth month-over-month bigger than those with average grade</strong></li> </h3>

While the properties with average grade have a growth of 0.74% a month, on average, those with high grade grow at 1.20% a month, a difference of 60.87%. Then they can be a good addition to the portfolio in terms of medium to long term investment.

<h3><strong><li>Properties in bad conditions are 66.54 % more cheap than those in good conditions</strong></li></h3>

They can be acquired with a low investment and renovated for sale, maintaining a good profit.
</ul>

<i>All the hyphothesis tested can be be check in the [notebook](https://github.com/lavinomenezes/House_rocket_insight_project/blob/main/notebooks/House_rocket_notebook.ipynb) to see they full description, or a brief overview on [Hypothesis](https://github.com/lavinomenezes/House_rocket_insight_project/blob/main/Hypothesis.md)</i>

## Business results

There are a total of 21,461 available properties to purchase, of this amount 10,498 were suggested to buy. The table below describes the financial results.


| Available Properties | Suggestions to buy | Investiment | Return | Profit |
|:----------------------:|:--------------------:|:-------------:|:--------:|:--------:|
| 21,461 | 10,498 | $5,656,988,504.00 | $6,622,652,682.20 | $965,664,178.2 |




##  Conclusion

In this project it was suggested properties for buying and the price of selling as well hypothesis were tested to better understand the price behavior and the results was delivered to the CEO, the list of suggestions as well the main insights are available online at [House rocket insight report] to be accessed by the CEO and  other company’s members.







##  Next steps
<ul>
<li>Increase the  amount of relevant information about  the properties;</li>
<li>Explore the promising hypotheses further;</li>
<li>Test new hypothesis;</li>
<li>Explore machine learning models to predict the behavior of properties prices.</li>
</ul>
