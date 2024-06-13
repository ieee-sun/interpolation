# Interpolation for Missing Data

#### An overview to various Interpolation methods for missing data. Demo in Time-series records with NaN entries.


**Table of Contents**

[TOC]


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
> [Interpolation for Missing Data - Demo](https://github.com/ieee-sun/interpolation/blob/e3cc3d6d1db75e55bef3dafce4992c9e6f95e164/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html)


image -

---

Prepared & Published by Sun CHUNG, *SMIEEE* M.Sc. HKU - *colab w/ MIT-IDSS*

-----

README.md
End of File
