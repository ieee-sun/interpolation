# Interpolation for Missing Data

### An overview & demo of various Interpolation methods for missing data.

### Effective for Dynamic-detection(LIDAR/CFAR), Deep Image Sensor, and Time-series records with `NaN` entries.
<img src="https://github.com/ieee-sun/interpolation/assets/172009644/7766fc70-931b-45b4-b2c0-9a4b346ce0f9" width=999 alt="Motion-Detection Data" title="Motion-Detection Data, generated by Sun CHUNG, SMIEEE" style="opacity: 0.33;">

> Imputational trace with classical interpolation (Linear/Polynomial/Spline/Seasonal) and Machine Learning Methods.

### [**Contents**](https://github.com/ieee-sun/interpolation/blob/4c2bb574bbb4805d9ae468ae8bb9f81b804b10ac/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html)
> Click [**Download**](https://github.com/ieee-sun/interpolation/blob/4c2bb574bbb4805d9ae468ae8bb9f81b804b10ac/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html) to View, HTML
* [Basic] - Linear Interpolation
* [Advanced] - Curved Interpolation:
  * Polynomial Interpolation
  * Spline Interpolation
* Dealing with Seasonal Data:
  * Seasonal Decomposition of Time Series
  * Filling Missing Values Using Seasonal Decomposition
* Machine Learning for Imputation:
  * Using K-Nearest Neighbors to Impute Missing Values
* Notes for Data Engineers
* Demo & Comparison
  * [Interpolation for Missing Data - Detailed Demo](https://github.com/ieee-sun/interpolation/blob/4c2bb574bbb4805d9ae468ae8bb9f81b804b10ac/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html) (click Download to View)

<img src="https://github.com/ieee-sun/interpolation/assets/172009644/c40d4ed3-ee58-4c8d-ae5f-1a9bc245625c" width=999 alt="Interpolated Demo Charts" title="Interpolated Demo Charts, generated by Sun CHUNG, SMIEEE">

## [Basic] - Linear Interpolation
Linear interpolation is a simple and effective method for estimating missing values when the data is relatively smooth, and **exhibits linear trends** between data points.

## [Advanced] - Curved Interpolation:
- ### Polynomial Interpolation
  Polynomial interpolation fits a polynomial of specified order, or **complex curves** through the known data points, making it suitable for datasets with non-linear trends.
- ### Spline Interpolation
  Spline interpolation fits **piecewise polynomials** between data points, ensuring smooth transitions. It effectively captures **complex patterns** without the risk of overfitting.

## Dealing with Seasonal Data:
- ### Seasonal Decomposition of Time Series
- ### Filling Missing Values Using Seasonal Decomposition
  Seasonal decomposition is highly effective for **time series data** with clear seasonal patterns. It separates the data into `trend`, `seasonal`, and `residual` components, allowing for targeted imputation. Filling missing values using the `trend` component can be effective in **seasonal data**.

## Machine Learning for Imputation:
- ### Using K-Nearest Neighbors to Impute Missing Values
  KNN imputation is a versatile method that **estimates missing values based on the similarity to other data points**. It can capture local patterns in the data.

## Notes for Data Engineers
> Click [**Download**](https://github.com/ieee-sun/interpolation/blob/4c2bb574bbb4805d9ae468ae8bb9f81b804b10ac/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html) to View, HTML

## Demo & Comparison
- #### Download to View:
> [Interpolation for Missing Data - Demo (HTML, 3.3MB)](https://github.com/ieee-sun/interpolation/blob/4c2bb574bbb4805d9ae468ae8bb9f81b804b10ac/Interpolation%20for%20Missing%20Data%20-%20Overview%20-%20Demo.html)
> Comparison of 6 interpolation models with dataset and illustrations.
>
> [Python solution - Linear Interpolation (.py)](https://github.com/ieee-sun/interpolation/blob/13fbd9950ec0f5956be0f5268b93180b40d9d366/interpolation.py)
> 
> [Python solution - Polynomial Interpolation (.py)](https://github.com/ieee-sun/interpolation/blob/13fbd9950ec0f5956be0f5268b93180b40d9d366/polynomial.py)

> ###### Prepared & Published by:
> ##### Sun CHUNG, *SMIEEE* M.Sc. HKU - *colab w/ MIT-IDSS*

<img src="https://github.com/ieee-sun/interpolation/assets/172009644/22125ae5-0707-477e-8acc-5e4e4f4c585d" width=1004 alt="KNN Graphical Imputation" title="KNN Graphical Imputation, generated by Sun CHUNG, SMIEEE">
<img src="https://github.com/ieee-sun/interpolation/assets/172009644/05297e3d-7482-4422-8cf0-0bff4ba51c33" width=412 alt="Automobile Trajectory Prediction" title="KNN Graphical Imputation, generated by Koji Endo"> 
<img src="https://github.com/ieee-sun/interpolation/assets/172009644/4df2c81b-5481-4965-a933-8068cb07b637" width=412 alt="MIMO FMCW Deep Image Radar Detection" title="MIMO FMCW Deep Image Radar Detection">

---
