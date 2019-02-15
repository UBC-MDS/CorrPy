# CorrPy

Latest Update Date: 2019 Feb.

## Overview

This package is developed to help users calculate correlation coefficients and covariance matrix of a given data with missing values. In order to implement correlation coefficients and covariance matrix, the standard deviation of the data is needed however the world of data is not always clean and tidy. Python's `numpy` fails to return standard deviation and calculation of the correlation coefficients when the data has missing values. This package aims to overcome this obstacle and help users handle missing values when calculating correlation coefficients and covariance matrix. `CorrPy` uses likewise deletion method to handle missing values: removing the rows of a data frame where the missing values are present.

*Note: If the course timeline permits, `CorrPy` will handle missing values via single manipulation with mean value: replacing the missing values with the mean of existing values.*

- [Python Version Link](https://github.com/UBC-MDS/CorrPy)
- [R Version Link](https://github.com/UBC-MDS/CorrR)

### Team

| Name  | Slack Handle | Github.com | Link |
| :------: | :---: | :----------: | :---: |
| KERA YUCEL | `@KERA YUCEL` | `@K3ra-y` | [Kera's link](https://github.com/K3ra-y/Corrpy)|
| GOPALAKRISHNAN ANDIVEL | `@Krish` | `@Gopsathvik` | [Krish's link](https://github.com/Gopsathvik/CorrPy)|
| WEISHUN DENG | `@Wilson Deng` | `@xiaoweideng` | [Wilson's link](https://github.com/xiaoweideng/Corrpy)|
| Mengda Yu | `@Mengda(Albert) Yu` | `@mru4913` | [Albert's link](https://github.com/mru4913/Corrpy) |


## Installation

`CorrPy` can be installed with pip in a command window:

`pip install git+https://github.com/UBC-MDS/CorrPy.git`


## Functions

### Standard Deviation (`std_plus`)

Standard deviation calculates how close the data points to the mean, in which an insight for the variation of the data points. This function would automatically handle the missing values in the input.

<BR>
<a href="https://www.codecogs.com/eqnedit.php?latex=s&space;=&space;\sqrt{\frac{\sum(x-\overline{x})^2}{n-1}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s&space;=&space;\sqrt{\frac{\sum(x-\overline{x})^2}{n-1}}" title="s = \sqrt{\frac{\sum(x-\overline{x})^2}{n-1}}" /></a>
<BR>

`std_plus` will omit frustration from workflows.

<BR>
 
### *Example*:

```Python
>>> import CorrPy
>>> x = [1,2, np.nan, 4, np.nan, 6]
>>> std_plus(x)
array([1.920286436967152])

>>> y = [1,2, np.inf, 4, np.nan, 6, "a"]
>>> np.std_plus(y)
array([1.920286436967152])
```


<BR>

 ### Correlation Coefficients (`corr_plus`)

Correlation coefficients calculates the relationship between two variables as well as the magnitude of this relationship. This function would automatically handle the missing values in the input.
<BR>

<a href="https://www.codecogs.com/eqnedit.php?latex=r&space;=&space;\frac{1}{n-1}(\frac{\sum(x-\overline{x})(y-\overline{y})}{s_{x}s_{y}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r&space;=&space;\frac{1}{n-1}(\frac{\sum(x-\overline{x})(y-\overline{y})}{s_{x}s_{y}})" title="r = \frac{1}{n-1}(\frac{\sum(x-\overline{x})(y-\overline{y})}{s_{x}s_{y}})" /></a>

<BR>
 
### *Example*:

```Python
>>> import CorrPy
>>> x = [1,2,np.nan,4,5]
>>> y = [-6,-7,-8,9,True]
>>> corr_plus(x,y)
array([0.7391090892601785])
```


<BR>
 
### Covariance Matrix (`cov_mx`)

A Covariance matrix displays the variance and covariance together. This function would use the above two functions.

<BR>
<a href="https://www.codecogs.com/eqnedit.php?latex=Cov(X,Y)&space;=&space;\frac{\sum(x-\overline{x})(y-\overline{y})}{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Cov(X,Y)&space;=&space;\frac{\sum(x-\overline{x})(y-\overline{y})}{N}" title="Cov(X,Y) = \frac{\sum(x-\overline{x})(y-\overline{y})}{N}" /></a>
<BR>
A covariance matrix displays the variance and covariance together. The diagonal elements represent the variances and the covariances are represented by the other elements in the matrix shown below.
<BR>

<a href="https://www.codecogs.com/eqnedit.php?latex=\Sigma&space;=&space;\begin{bmatrix}Var(X_1)&space;&&space;Cov(X_1&space;X_2)&space;&\cdots&\cdots&space;&\cdots&space;&&space;Cov(X_1&space;X_k)\\&space;Cov(X_2&space;X_1)&space;&Var(X_2)&&space;\cdots&space;&\cdots&space;&\cdots&space;&&space;\cdots\\&space;\cdots&space;&&space;\cdots&space;&\ddots&space;&\cdots&space;&\cdots&space;&&space;\cdots\\&space;\cdots&space;&&space;\cdots&space;&\cdots&space;&\ddots&space;&\cdots&space;&&space;\cdots\\&space;Cov(X_{k-1}&space;X_1)&space;&&space;\cdots&space;&\cdots&space;&\cdots&space;&Var(X_{k-1})&space;&&space;\cdots\\&space;Cov(X_k&space;X_1)&space;&&space;Cov(X_k&space;X_2)&space;&\cdots&space;&\cdots&space;&\cdots&space;&&space;Var(X_k)\\\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Sigma&space;=&space;\begin{bmatrix}Var(X_1)&space;&&space;Cov(X_1&space;X_2)&space;&\cdots&\cdots&space;&\cdots&space;&&space;Cov(X_1&space;X_k)\\&space;Cov(X_2&space;X_1)&space;&Var(X_2)&&space;\cdots&space;&\cdots&space;&\cdots&space;&&space;\cdots\\&space;\cdots&space;&&space;\cdots&space;&\ddots&space;&\cdots&space;&\cdots&space;&&space;\cdots\\&space;\cdots&space;&&space;\cdots&space;&\cdots&space;&\ddots&space;&\cdots&space;&&space;\cdots\\&space;Cov(X_{k-1}&space;X_1)&space;&&space;\cdots&space;&\cdots&space;&\cdots&space;&Var(X_{k-1})&space;&&space;\cdots\\&space;Cov(X_k&space;X_1)&space;&&space;Cov(X_k&space;X_2)&space;&\cdots&space;&\cdots&space;&\cdots&space;&&space;Var(X_k)\\\end{bmatrix}" title="\Sigma = \begin{bmatrix}Var(X_1) & Cov(X_1 X_2) &\cdots&\cdots &\cdots & Cov(X_1 X_k)\\ Cov(X_2 X_1) &Var(X_2)& \cdots &\cdots &\cdots & \cdots\\ \cdots & \cdots &\ddots &\cdots &\cdots & \cdots\\ \cdots & \cdots &\cdots &\ddots &\cdots & \cdots\\ Cov(X_{k-1} X_1) & \cdots &\cdots &\cdots &Var(X_{k-1}) & \cdots\\ Cov(X_k X_1) & Cov(X_k X_2) &\cdots &\cdots &\cdots & Var(X_k)\\\end{bmatrix}" /></a>


<BR>
 
### *Example*:

```Python
>>> import CorrPy
>>> x = [1,2,np.nan,4,5]
>>> y = [-6,-7,-8,9,True]
>>> cov_mx([x,y])
array([[ 2.33333333, 12.66666667],
       [12.66666667, 80.33333333]])
```


<BR>
 
### *How does `CorrPy` package fits into the Python ecosystem?*

  Following functions are already present in Python ecosystem. However, missing values are not being handles for the following functions and `CorrPy` package will implement calculation of standard deviation, correlation coefficients and covariance matrix.

Python Standard Deviation: https://docs.scipy.org/doc/numpy-1.14.2/reference/generated/numpy.std.html

Python Correlation Coefficients: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.corrcoef.html

Python Covariance Matrix: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.cov.html

## Milestone Progress

| Milestone | Tasks |
|---|---|
|Milestone 1 | [Proposal](https://github.com/UBC-MDS/CorrPy/blob/master/docs/proposal.md)|
|Milestone 2 | [Function Code](https://github.com/UBC-MDS/CorrPy/tree/master/CorrPy)|
|            | [Test Code](https://github.com/UBC-MDS/CorrPy/tree/master/CorrPy/test)|
