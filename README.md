# Interpolation for Missing Data - OVERVIEW

#### An overview to various Interpolation methods for missing data. Demo in Time-series records with `NaN` entries.
![random_nan_imputated](https://github.com/ieee-sun/interpolation/assets/172009644/7766fc70-931b-45b4-b2c0-9a4b346ce0f9)
**Table of Contents**
* [Basic] - Linear Interpolation
* [Advanced] - Curved Interpolation:
  * Polynomial Interpolation
  * Spline Interpolation
* Dealing with Seasonal Data:
  * Seasonal Decomposition of Time Series
  * Filling Missing Values Using Seasonal Decomposition
* Machine Learning for Imputation:
  * Using K-Nearest Neighbors to Impute Missing Values
*Notes for Data Engineers
* Demo & Comparison
  >  [Interpolation for Missing Data - Detailed Demo](https://github.com/ieee-sun/interpolation/blob/4c2bb574bbb4805d9ae468ae8bb9f81b804b10ac/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html)
(Download to View)

![interpolated_charts_demo](https://github.com/ieee-sun/interpolation/assets/172009644/c40d4ed3-ee58-4c8d-ae5f-1a9bc245625c)


## [Bacic] - Linear Interpolation
Linear interpolation is a simple and effective method for estimating missing values when the data is relatively smooth and **exhibits linear trends** between data points.

## [Advanced] - Curved Interpolation:
- ### Polynomial Interpolation
Polynomial interpolation fits a polynomial of a specified order, or **complex curves** through the known data points, making it suitable for datasets with non-linear trend.
- ### Spline Interpolation
Spline interpolation fits **piecewise polynomials** between data points, ensuring smooth transitions. It is effective for capturing **complex patterns** without the risk of overfitting.

## Dealing with Seasonal Data:
- ### Seasonal Decomposition of Time Series
- ###Filling Missing Values Using Seasonal Decomposition
Seasonal decomposition is highly effective for **time series data** with clear seasonal patterns. It separates the data into `trend`, `seasonal`, and `residual` components, allowing for targeted imputation. Filling missing values using the `trend` component can be effective in **seasonal data**.

## Machine Learning for Imputation:
- ### Using K-Nearest Neighbors to Impute Missing Values
KNN imputation is a versatile method that **estimates missing values based on the similarity to other data points**. It can capture local patterns in the data.

## Notes for Data Engineers
## Demo & Comparison
- #### Download to View:
> [Interpolation for Missing Data - Demo](https://github.com/ieee-sun/interpolation/blob/4c2bb574bbb4805d9ae468ae8bb9f81b804b10ac/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html)


> Prepared & Published by Sun CHUNG, *SMIEEE* M.Sc. HKU - *colab w/ MIT-IDSS*

---

README.md
End of File
