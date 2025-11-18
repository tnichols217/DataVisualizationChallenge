# CSDS 313 Data Visualization Challenge

Aidan Bugayong, Sam Lin, Wolf Mermelstein, Trevor Nichols

This project aims to improve upon an existing data visualization info graphic about Cleveland.

## Problems with Original Visualization

![Cost of living in Cleveland infographic](https://livingcost.org/assets/photo/cost/united-states/oh/cleveland.jpg)
![Cost of living in San Diego infographic](https://livingcost.org/assets/photo/cost/united-states/ca/san-diego.jpg)

### Arbitrary nonlinear scaling of values

The percentage bar system the original visualization used was rather poorly designed; Despite Cleveland being ranked 1793 (low end) but appears to be a high percentage of the bar. Alternatively, looking at it from purely a numerical perspective the increase of the percentage bar is not linear and feels arbitrary.

### Unintuitive Ranking System and Coloring System

The total rent for Cleveland appears orange, which would typically indicate that increasing the rank would make it more red and thus only 

### Comparing between salary and cost of living is difficult

Although a breakdown of a few key points of costs are listed, the combined metric is spatially positioned the furthest from the income, which are the two values you likely would like to compare. A ratio in its place would be much more interpretable for the meaning of the data.

### Misleading emojis

The various aspects that are being compared for each city are assigned a loosely related emoji that adds no value to the comparison and may even confuse readers, with rent being represented as a moneybag while salary is a credit card, which is completely unintuitive.

## Data Source Validity

### Numbeo

[https://www.numbeo.com/quality-of-life/region_rankings.jsp](https://www.numbeo.com/quality-of-life/region_rankings.jsp)

Numbeo’s mission is to give individuals and businesses accurate and up to date information on various socio-economic factors for cities across the globe. The research and information at Numbeo is not influenced by any government authorities or organizations and is used as a data source by numerous international newspapers and magazines, including BBC, Time, The Week, Forbes, The Economist, Business Insider, San Francisco Chronicle, The New York Times, The Telegraph, The Age, The Sydney Morning Herald, China Daily, The Washington Post, USA Today and many more.

### Apartment List

[https://www.apartmentlist.com/research/category/data-rent-estimates](https://www.apartmentlist.com/research/category/data-rent-estimates)

Apartment List’s rental estimates are widely trusted because they are built on a large, continuously updated dataset drawn directly from real, active rental listings across the US. Their methodology is transparent and publicly documented, allowing researchers, journalists, and policymakers to verify how the estimates are produced. Apartment List regularly publishes national and city-level housing reports using this data, and their work is frequently cited by major news outlets and research organizations that rely on accurate housing market information. Because their data is independent, systematically collected, and backed by a rigorous estimation process, Apartment List serves as a reliable source for understanding rental trends and comparing cities like Cleveland to the broader U.S. market.

## Process

We used Numbeo’s data on the Quality of Life Index and related statistics, including the Health Care Index, Cost of Living Index, and Property Price-to-Income Ratio. Since we aimed to improve the original visualization, we filtered the dataset to include only U.S. cities. Additionally, we incorporated data from ApartmentList.com on average apartment prices by city and again restricted the dataset to U.S. cities to identify where Cleveland stands.

To provide clearer context for Cleveland’s position in the rankings, we used box plots. These plots allow us to compare Cleveland’s data point with the median, upper and lower quartiles, and overall range. This gives a more informative view of Cleveland’s relative standing than a simple percentage bar.

Additionally, we improved upon Numbeo’s Quality of life statistic which was calculated with the following formula:

```javascript
index.main = Math.max(0,
100
+ (purchasingPowerInclRentIndex / 2.5)
- (houseToIncomeRatio * 1.0)
- (costOfLivingIndex / 10)
+ (safetyIndex / 2.0)
+ (healthIndex / 2.5)
- (trafficTimeIndex / 2.0)
- (pollitionIndex * 2.0 / 3.0)
+ (climateIndex / 3.0)
)
```

This formula may appear problematic as the weightings of the different columns appear quite arbitrary and also at times applies similar weights to columns of vastly different scales and distributions. As a result, we performed quantile normalization on the columns and then added or subtracted the values depending on if the column was good or bad. This results in each column being weighted equally and also each column having the same power as every other column (because the values now come from the same distribution).

## Improvements

As seen in our graphic, all aspects we compare are easy to interpret in comparison with other US cities. We do not utilize any misleading emoji, keep the graph simple and interpretable, and highlight our target city with color. The distributions of the various aspects are also directly visible, making comparison and significance easier to grasp at a quick glance. Lastly, instead of directly comparing monetary values, we utilize interpretable quality indicators, like our housing to income ratio, cost of living index, and health care index.

Our graphic does not try to mislead and assign a “ranking” to a city—something completely unrepresentative of such a complicated concept, and additionally calculate our QOL index by summing on the normalized data from 4 positive and negative metrics: purchasing power, safety index, health care, and climate; and cost of living, property to income ratio, traffic commute time, and pollution.

## Code and Work

https://github.com/tnichols217/DataVisualizationChallenge

All of our work is uploaded to GitHub with complete instructions on how the code is run, complete with development environments and documentation.

## Works Cited

Cleveland, OH: Cost of living, prices for Rent & Food [2025]. (2025). Retrieved from [https://livingcost.org/cost/united-states/oh/](https://livingcost.org/cost/united-states/oh/)

Data & Rent estimates. (n.d.). Retrieved from [https://www.apartmentlist.com/research/category/data-rent-estimates](https://www.apartmentlist.com/research/category/data-rent-estimates)

Quality of Life components,  Cost of Living Index, Property Price to Income Ratio, Traffic Commute Time Index, and Health Care Index. (n.d.). Retrieved from [https://www.numbeo.com/quality-of-life/region_rankings.jsp](https://www.numbeo.com/quality-of-life/region_rankings.jsp)
