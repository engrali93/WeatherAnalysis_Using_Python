# WeatherAnalysis_Using_Python
 Rainfall Prediction Using Linear Regression Model using python
 
 ## What is Regression
 Typically, you need regression to answer whether and how some phenomenon influences the other or how several variables are related. For example, you can use it to determine if and to what extent the experience or gender impact salaries.

Regression is also useful when you want to forecast a response using a new set of predictors. For example, you could try to predict electricity consumption of a household for the next hour given the outdoor temperature, time of day, and number of residents in that household.

Regression is used in many different fields: economy, computer science, social sciences, and so on. Its importance rises every day with the availability of large amounts of data and increased awareness of the practical value of data.


 ### Linear Regression
 When implementing linear regression of some dependent variable ๐ฆ on the set of independent variables ๐ฑ = (๐ฅโ, โฆ, ๐ฅแตฃ), where ๐ is the number of predictors, you assume a linear relationship between ๐ฆ and ๐ฑ: ๐ฆ = ๐ฝโ + ๐ฝโ๐ฅโ + โฏ + ๐ฝแตฃ๐ฅแตฃ + ๐. This equation is the regression equation. ๐ฝโ, ๐ฝโ, โฆ, ๐ฝแตฃ are the regression coefficients, and ๐ is the random error.

Linear regression calculates the estimators of the regression coefficients or simply the predicted weights, denoted with ๐โ, ๐โ, โฆ, ๐แตฃ. They define the estimated regression function ๐(๐ฑ) = ๐โ + ๐โ๐ฅโ + โฏ + ๐แตฃ๐ฅแตฃ. This function should capture the dependencies between the inputs and output sufficiently well.

The estimated or predicted response, ๐(๐ฑแตข), for each observation ๐ = 1, โฆ, ๐, should be as close as possible to the corresponding actual response ๐ฆแตข. The differences ๐ฆแตข - ๐(๐ฑแตข) for all observations ๐ = 1, โฆ, ๐, are called the residuals. Regression is about determining the best predicted weights, that is the weights corresponding to the smallest residuals.

To get the best weights, you usually minimize the sum of squared residuals (SSR) for all observations ๐ = 1, โฆ, ๐: SSR = ฮฃแตข(๐ฆแตข - ๐(๐ฑแตข))ยฒ. This approach is called the method of ordinary least squares.


## cleanDataSet
this program is used to clean the data and drop the unwanted columns. The purpose of doing this is to make program run fast and more efficient when we will going to place linear regression on it.

## Result
The program is divided into two methods.
1) In first we focus on one factor for rain and that is precipitation

as you can see the graph mentioned below.

![alt text](https://github.com/engrali93/WeatherAnalysis_Using_Python/blob/main/graph%20output/Figure_1.png)


2) We use filter to evaluate via different factor

as mentioned in subplot diagram below

![alt text](https://github.com/engrali93/WeatherAnalysis_Using_Python/blob/main/graph%20output/Figure_2.png)

